from sys import exit

import pygame
from clipboard import paste

from algorithms.bogo_sort import bogo_sort
from algorithms.bubble_sort import bubble_sort
from algorithms.heap_sort import heap_sort
from algorithms.insertion_sort import insertion_sort
from algorithms.merge_sort import merge_sort
from algorithms.quick_sort import quick_sort
from algorithms.radix_sort import radix_sort
from algorithms.selection_sort import selection_sort
from algorithms.shell_sort import shell_sort
from block import *
from constants import *
from grid import Grid
from image import ImageProcessing
from ui_elements.button import Button
from ui_elements.slider import Slider
from ui_elements.switch import Switch
from ui_elements.textbox import TextBox


class App:
    def __init__(self) -> None:
        pygame.init()

        # Pygame initialisation 
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Sorting Algorithm Visualisation")
        self.icon = pygame.image.load("images/app_assets/ICON.png").convert_alpha()
        pygame.display.set_icon(self.icon)

        # Font Initialization initialisation 
        self.title_font = pygame.font.SysFont("Times New Roman", 50)
        self.button_font = pygame.font.SysFont("Trebuchet MS", 15, bold=True)
        self.gui_font = pygame.font.SysFont("Cascadia Code", 25)

        # Pygame Utilities initialisation 
        self.clock = pygame.time.Clock()
        self.running = True

        # Grid Related initialisation 
        self.gridlines_switch = Switch(
            "ON",
            "OFF",
            GREEN,
            RED,
            self.button_font,
            (300, 25),
            (BARRIER_PADDING_X_LEFT / 2, HEIGHT_MIDPOINT - 188),
        )
        self.grid_slider = Slider((BARRIER_PADDING_X_LEFT / 2, HEIGHT_MIDPOINT - 212.5), (300, 25), 0.5, 2, 50)
        self.row_and_col_val = None
        
        # Image Related initialisation 
        self.img = ImageProcessing()
        self.img_path = TextBox(25, ((BARRIER_PADDING_X_LEFT / 2) - 100, HEIGHT - 50), BLACK, self.gui_font)
        self.textbox_switch = Switch(
            "ADD",
            "DEL",
            GREEN,
            RED,
            self.button_font,
            (50, 25),
            ((BARRIER_PADDING_X_LEFT / 2) - 125, HEIGHT - 50),
        )

        # Shuffling, Sorting and Algorithm selection initialisation 
        self.index_grid_pos = None
        self.sort_time_start = 0
        self.sort_time_end = 0
        self.sort_time_elapsed = 0
        
        self.shuffle_button = Button(
            "SHUFFLE",
            GREEN,
            LIGHT_GREEN,
            self.button_font,
            (100, 50),
            ((BARRIER_PADDING_X_LEFT / 2) - 100, HEIGHT_MIDPOINT + 200),
        )
        self.sort_button = Button(
            "SORT",
            GREEN,
            LIGHT_GREEN,
            self.button_font,
            (100, 50),
            (BARRIER_PADDING_X_LEFT / 2, HEIGHT_MIDPOINT + 200),
        )
        self.stop_button = Button(
            "STOP",
            RED,
            LIGHT_RED,
            self.button_font,
            (100, 50),
            ((BARRIER_PADDING_X_LEFT / 2) + 100, HEIGHT_MIDPOINT + 200)
        )
        
        self.bogo_button = Button(
            "Bogo",
            DARK_BLUE,
            LIGHT_BLUE,
            self.button_font,
            (100, 50),
            ((BARRIER_PADDING_X_LEFT / 2) - 100, HEIGHT_MIDPOINT - 50),
        )
        
        self.bubble_button = Button(
            "Bubble",
            DARK_BLUE,
            LIGHT_BLUE,
            self.button_font,
            (100, 50),
            (BARRIER_PADDING_X_LEFT / 2, HEIGHT_MIDPOINT - 50),
        )
        self.selection_button = Button(
            "Selection",
            DARK_BLUE,
            LIGHT_BLUE,
            self.button_font,
            (100, 50),
            ((BARRIER_PADDING_X_LEFT / 2) + 100, HEIGHT_MIDPOINT - 50),
        )
        self.insertion_button = Button(
            "Insertion",
            DARK_BLUE,
            LIGHT_BLUE,
            self.button_font,
            (100, 50),
            ((BARRIER_PADDING_X_LEFT / 2) - 100, HEIGHT_MIDPOINT),
        )
        self.shell_button = Button(
            "Shell",
            DARK_BLUE,
            LIGHT_BLUE,
            self.button_font,
            (100, 50),
            (BARRIER_PADDING_X_LEFT / 2, HEIGHT_MIDPOINT),
        )
        self.heap_button = Button(
            "Heap",
            DARK_BLUE,
            LIGHT_BLUE,
            self.button_font,
            (100, 50),
            ((BARRIER_PADDING_X_LEFT / 2) + 100, HEIGHT_MIDPOINT),
        )
        self.merge_button = Button(
            "Merge",
            DARK_BLUE,
            LIGHT_BLUE,
            self.button_font,
            (100, 50),
            ((BARRIER_PADDING_X_LEFT / 2) - 100, HEIGHT_MIDPOINT + 50),
        )
        self.quick_button = Button(
            "Quick",
            DARK_BLUE,
            LIGHT_BLUE,
            self.button_font,
            (100, 50),
            (BARRIER_PADDING_X_LEFT / 2, HEIGHT_MIDPOINT + 50),
        )
        
        self.radix_button = Button(
            "Radix",
            DARK_BLUE,
            LIGHT_BLUE,
            self.button_font,
            (100, 50),
            ((BARRIER_PADDING_X_LEFT / 2) + 100, HEIGHT_MIDPOINT + 50),
        )
        
        self.chosen_algo = None
        self.time_complexity = None
        self.sort_generator = None
        
        # Conditionals initialisation 
        self.img_added = False
        self.selected_grid_size = False
        self.sorting = False
        self.sorted = True
        
        # Surfaces initialisation 
        self.options_surface = pygame.Surface((325, 75))
        self.options_surface_rect = self.options_surface.get_rect(center=((BARRIER_PADDING_X_LEFT / 2, HEIGHT_MIDPOINT - 200)))
        
        self.algo_box_surface = pygame.Surface((325, 175))
        self.algo_box_surface_rect = self.algo_box_surface.get_rect(center=(BARRIER_PADDING_X_LEFT / 2, HEIGHT_MIDPOINT))
        
        self.control_box_surface = pygame.Surface((325, 75))
        self.control_box_surface_rect = self.control_box_surface.get_rect(center=((BARRIER_PADDING_X_LEFT / 2, HEIGHT_MIDPOINT + 200)))
        
        self.information_surface = pygame.Surface((325, 125))
        self.information_surface_rect = self.information_surface.get_rect(center=((WIDTH - 275, HEIGHT_MIDPOINT - 175.75)))
        
        # Text initialisation        
        self.invalid_entry_txt = self.gui_font.render("INVALID ENTRY!", True, RED)
        self.invalid_entry_txt_rect = self.invalid_entry_txt.get_rect(center=(WIDTH_MIDPOINT, BARRIER_PADDING_Y_TOP // 2))
        
        self.invalid_path_txt = self.gui_font.render("DIRECTORY DOES NOT EXIST!", True, RED)
        self.invalid_path_txt_rect = self.invalid_path_txt.get_rect(center=(WIDTH_MIDPOINT, BARRIER_PADDING_Y_TOP // 2))
        
        self.chosen_algo_txt = self.gui_font.render(f"Algorithm: {self.chosen_algo}", True, WHITE)
        self.chosen_algo_txt_rect = self.chosen_algo_txt.get_rect(midleft=((WIDTH - 412.5, HEIGHT_MIDPOINT - 212.5)))
        
        self.time_complexity_txt = self.gui_font.render(f"Time Complexity: {self.time_complexity}", True, WHITE)
        self.time_complexity_txt_rect = self.chosen_algo_txt.get_rect(midleft=(WIDTH - 412.5, HEIGHT_MIDPOINT - 188))
        
        self.grid_size_txt = self.gui_font.render(f"Grid Size: {self.row_and_col_val}x{self.row_and_col_val}", True, WHITE)
        self.grid_size_txt_rect = self.grid_size_txt.get_rect(midleft=(WIDTH - 412.5, HEIGHT_MIDPOINT - 163.5))
        
        self.sorting_time_txt = self.gui_font.render(f"Sorting Time: {self.sort_time_elapsed:.2f} seconds", True, WHITE)
        self.sorting_time_txt_rect = self.grid_size_txt.get_rect(midleft=(WIDTH - 412.5, HEIGHT_MIDPOINT - 139))
            
        # Arrays initialisation 
        self.algo_buttons_arr = [
            self.bogo_button,
            self.bubble_button,
            self.selection_button,
            self.insertion_button,
            self.shell_button,
            self.heap_button,
            self.merge_button,
            self.quick_button,
            self.radix_button,
        ]
        
        self.control_buttons_arr = [
            self.shuffle_button,
            self.sort_button,
            self.stop_button,
            self.textbox_switch,
            self.gridlines_switch,
        ]
        
        self.surface_arr = [
            [self.options_surface, self.options_surface_rect],
            [self.algo_box_surface, self.algo_box_surface_rect],
            [self.control_box_surface, self.control_box_surface_rect],
            [self.information_surface, self.information_surface_rect],
        ]
        
        self.text_arr = [
            [self.chosen_algo_txt, self.chosen_algo_txt_rect],
            [self.time_complexity_txt, self.time_complexity_txt_rect],
            [self.grid_size_txt, self.grid_size_txt_rect],
            [self.sorting_time_txt, self.sorting_time_txt_rect],
        ]

    def run(self):
        while self.running:
            self.update()
            self.draw()
        self.close()

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.img.del_images()
                self.running = False
        
        # Grid Setup
        self.grid_slider.render(self.screen)

        if not self.img_added:
            self.grid_slider.move_slider()
            self.row_and_col_val = self.grid_slider.get_value()
            self.grid = Grid(GRID_WIDTH, GRID_HEIGHT, self.row_and_col_val, self.row_and_col_val)
            self.grid_size_txt = self.gui_font.render(f"Grid Size: {self.row_and_col_val} x {self.row_and_col_val}", True, WHITE)
            self.grid_size_txt_rect = self.grid_size_txt.get_rect(midleft=(WIDTH - 412.5, HEIGHT_MIDPOINT - 163.5))

        # Gridlines Transparency
        self.gridlines_switch.get_clicked()

        if self.gridlines_switch.active:
            self.grid.set_alpha_max()
        else:
            self.grid.set_alpha_min()

        # Image processing and setup
        if not self.sorting:
            self.textbox_switch.get_clicked()

        if self.textbox_switch.active:
            self.img_path.set_text(paste())
            self.grid.block_objects.clear()
            self.img_added = False
        else:
            if not self.img_added:
                try:
                    if self.img.verify_extension(r"{}".format(paste())):
                        self.img.update_img(paste())
                        self.img.split_into_blocks(
                            self.grid.rows,
                            self.grid.columns,
                            self.grid.row_spacing,
                            self.grid.column_spacing,
                        )
                        for i in self.img.blocks:
                            block = Block(i[0], i[1], i[2], self.grid.row_spacing, self.grid.column_spacing, i[3],)
                            self.grid.block_objects.append(block)
                            
                        self.index_grid_pos = get_index_grid_pos(self.grid.block_objects)
                        self.img_added = True
                    else:
                        self.screen.blit(self.invalid_entry_txt, self.invalid_entry_txt_rect) #Invalid file format attempted to be uploaded.
                except FileNotFoundError:
                    self.screen.blit(self.invalid_path_txt, self.invalid_path_txt_rect) #Accepted file format, but file destination doesn't exist.

        # Choosing Algorithm
        sort_dict = {
            self.bubble_button: (bubble_sort(self.grid.block_objects), "Bubble Sort", "O(n^2)"),
            self.bogo_button: (bogo_sort(self.grid.block_objects, self.index_grid_pos), "Bogo Sort", "O((n+1)!)"),
            self.selection_button: (selection_sort(self.grid.block_objects), "Selection Sort", "O(n^2)"),
            self.insertion_button: (insertion_sort(self.grid.block_objects), "Insertion Sort", "O(n^2)"),
            self.shell_button: (shell_sort(self.grid.block_objects), "Shell Sort", "O(n^1.5)"),
            self.heap_button: (heap_sort(self.grid.block_objects), "Heap Sort", "O(n log n)"),
            self.merge_button: (merge_sort(self.grid.block_objects, self.index_grid_pos), "Merge Sort", "O(n log n)"),
            self.quick_button: (quick_sort(self.grid.block_objects), "Quick Sort", "O(n log n)"),
            self.radix_button: (radix_sort(self.grid.block_objects, self.index_grid_pos), "Radix Sort", "O(n)"),
            }
        
        for button in self.algo_buttons_arr:
            if self.img_added:
                button.get_clicked()
            
            if button.clicked and not self.sorting:
                self.sort_generator, self.chosen_algo, self.time_complexity = sort_dict[button]
                self.sort_time_elapsed = 0
            
            self.chosen_algo_txt = self.gui_font.render(f"Algorithm: {self.chosen_algo}", True, WHITE)
            self.chosen_algo_txt_rect = self.chosen_algo_txt.get_rect(midleft=((WIDTH - 412.5, HEIGHT_MIDPOINT - 212.5)))
            
            self.time_complexity_txt = self.gui_font.render(f"Time Complexity: {self.time_complexity}", True, WHITE)
            self.time_complexity_txt_rect = self.chosen_algo_txt.get_rect(midleft=(WIDTH - 412.5, HEIGHT_MIDPOINT - 188))
            
            self.sorting_time_txt = self.gui_font.render(f"Sorting Time: {self.sort_time_elapsed:.2f} seconds", True, WHITE)
            self.sorting_time_txt_rect = self.grid_size_txt.get_rect(midleft=(WIDTH - 412.5, HEIGHT_MIDPOINT - 139))

        for button in self.control_buttons_arr:
            if self.img_added:
                button.get_clicked()
                
            # Shuffling
            if self.shuffle_button.clicked and not self.sorting:
                shuffle_pos(self.grid.block_objects, self.index_grid_pos)
                self.sorted = False
                self.shuffle_button.clicked = False
        
            # Sorting
            if not self.sorted and self.sort_button.clicked and self.sort_generator:
                    self.sort_time_start = pygame.time.get_ticks()
                    self.sorting = True
            if self.sorting:
                try:
                    next(self.sort_generator)
                except StopIteration:
                    self.sorted = True
                    self.sorting = False
                    self.sort_generator = None
                    self.sort_time_end = pygame.time.get_ticks()
                    self.sort_time_elapsed = (self.sort_time_end - self.sort_time_start) / 1000 # ticks are measured in milliseconds
                    self.sorting_time_txt = self.gui_font.render(f"Sorting Time: {self.sort_time_elapsed:.2f} seconds", True, WHITE)
                    self.sorting_time_txt_rect = self.grid_size_txt.get_rect(midleft=(WIDTH - 412.5, HEIGHT_MIDPOINT - 139))
        
            # Stopping
            if self.stop_button.clicked:
                self.sorting = False
        
        # Updates to Images on screen
        for block in self.grid.block_objects:
            block.draw_block(self.grid.image_surface)

        # Update Arrarys
        self.surface_arr = [
            [self.options_surface, self.options_surface_rect],
            [self.algo_box_surface, self.algo_box_surface_rect],
            [self.control_box_surface, self.control_box_surface_rect],
            [self.information_surface, self.information_surface_rect],
        ]
        
        self.text_arr = [
            [self.chosen_algo_txt, self.chosen_algo_txt_rect],
            [self.time_complexity_txt, self.time_complexity_txt_rect],
            [self.grid_size_txt, self.grid_size_txt_rect],
            [self.sorting_time_txt, self.sorting_time_txt_rect],
        ]
        
        
        self.clock.tick(FPS)
        pygame.display.update()
        
    # Draws the grid, textbox, surfaces and text to the screen.
    def draw(self):
        # Grid
        self.screen.fill(DARK_GRAY)
        self.screen.blit(self.grid.get_images()[0], self.grid.get_images()[1])
        self.screen.blit(self.grid.get_surface_and_rect()[0], self.grid.get_surface_and_rect()[1])

        # Textbox
        self.screen.blit(self.img_path.get_surface_and_rect()[0], self.img_path.get_surface_and_rect()[1],)

        # Image shuffling, sorting, stopping and algorithms
        for surface in self.surface_arr:
            self.screen.blit(surface[0], surface[1])
            pygame.draw.rect(self.screen, WHITE, surface[1], 3)
        
        for text in self.text_arr:
            self.screen.blit(text[0], text[1])
        
        for button in self.algo_buttons_arr:
            self.screen.blit(button.surface, button.surface_rect)
        
        for button in self.control_buttons_arr:
            self.screen.blit(button.surface, button.surface_rect)
        

    def close(self):
        pygame.quit()
        exit()


if __name__ == "__main__":
    app = App()
    app.run()
