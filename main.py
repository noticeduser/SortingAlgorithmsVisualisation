from sys import exit

import pygame
from clipboard import paste

from algorithms.bubble_sort import bubble_sort
from algorithms.heap_sort import *
from algorithms.insertion_sort import insertion_sort
from algorithms.merge_sort import *
from algorithms.quick_sort import *
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

        # Pygame Initialization
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Sorting Algorithm Visualisation")
        self.icon = pygame.image.load("images/app_assets/ICON.png").convert_alpha()
        pygame.display.set_icon(self.icon)

        # Font Initialization
        self.title_font = pygame.font.SysFont("Times New Roman", 50)
        self.button_font = pygame.font.SysFont("Trebuchet MS", 15, bold=True)
        self.gui_font = pygame.font.SysFont("Cascadia Code", 25)

        # Pygame Utilities
        self.clock = pygame.time.Clock()
        self.running = True

        # Grid Related
        self.options_screen = pygame.Surface((400, 125))
        self.options_screen.fill(BLACK)
        self.options_screen_rect = self.options_screen.get_rect(
            center=(WIDTH_MIDPOINT + 375, HEIGHT_MIDPOINT - 200)
        )

        self.gridlines_switch = Switch(
            "ON",
            "OFF",
            GREEN,
            RED,
            self.button_font,
            (50, 25),
            (WIDTH_MIDPOINT + 225, BARRIER_PADDING_Y + 75),
        )
        self.grid_slider = Slider((915, BARRIER_PADDING_Y + 25), (150, 25), 0.2, 2, 20)

        self.grid_enable_txt = self.gui_font.render("Gridlines", True, WHITE)
        self.grid_size_txt = self.gui_font.render("Grid Size", True, WHITE)

        # Image Related
        self.img = ImageProcessing()
        self.img_path = TextBox(
            25, (190, HEIGHT - BARRIER_PADDING_Y + 50), BLACK, self.gui_font
        )
        self.textbox_switch = Switch(
            "ADD",
            "DEL",
            GREEN,
            RED,
            self.button_font,
            (50, 25),
            (164, HEIGHT - BARRIER_PADDING_Y + 50),
        )

        self.invalid_entry = self.gui_font.render("Invalid Entry!", True, RED)
        self.invalid_entry_rect = self.invalid_entry.get_rect(
            bottomleft=(139, BARRIER_PADDING_Y - 5)
        )

        self.invalid_path = self.gui_font.render(
            "DIRECTORY DOES NOT EXIST!", True, RED
        )
        self.invalid_path_rect = self.invalid_path.get_rect(
            bottomleft=(139, BARRIER_PADDING_Y - 5)
        )

        # Shuffling and Sorting Image
        self.box_surface = pygame.Surface((400, 250))
        self.box_surface_rect = self.box_surface.get_rect(
            center=(WIDTH_MIDPOINT + 375, HEIGHT_MIDPOINT)
        )
        self.box_surface.fill(BLACK)

        self.index_grid_pos = None
        self.shuffle_button = Button(
            "SHUFFLE",
            GREEN,
            LIGHT_GREEN,
            self.button_font,
            (100, 50),
            (WIDTH_MIDPOINT + 250, HEIGHT_MIDPOINT + 75),
        )
        self.sort_button = Button(
            "SORT",
            GREEN,
            LIGHT_GREEN,
            self.button_font,
            (100, 50),
            (WIDTH_MIDPOINT + 500, HEIGHT_MIDPOINT + 75),
        )

        self.bubble_button = Button(
            "Bubble",
            DARK_BLUE,
            LIGHT_BLUE,
            self.button_font,
            (100, 50),
            (WIDTH_MIDPOINT + 250, HEIGHT_MIDPOINT - 75),
        )
        self.selection_button = Button(
            "Selection",
            DARK_BLUE,
            LIGHT_BLUE,
            self.button_font,
            (100, 50),
            (WIDTH_MIDPOINT + 375, HEIGHT_MIDPOINT - 75),
        )
        self.insertion_button = Button(
            "Insertion",
            DARK_BLUE,
            LIGHT_BLUE,
            self.button_font,
            (100, 50),
            (WIDTH_MIDPOINT + 500, HEIGHT_MIDPOINT - 75),
        )
        self.shell_button = Button(
            "Shell",
            DARK_BLUE,
            LIGHT_BLUE,
            self.button_font,
            (100, 50),
            (WIDTH_MIDPOINT + 250, HEIGHT_MIDPOINT),
        )
        self.heap_button = Button(
            "Heap",
            DARK_BLUE,
            LIGHT_BLUE,
            self.button_font,
            (100, 50),
            (WIDTH_MIDPOINT + 375, HEIGHT_MIDPOINT),
        )
        self.merge_button = Button(
            "Merge",
            DARK_BLUE,
            LIGHT_BLUE,
            self.button_font,
            (100, 50),
            (WIDTH_MIDPOINT + 500, HEIGHT_MIDPOINT),
        )
        self.quick_button = Button(
            "Quick",
            DARK_BLUE,
            LIGHT_BLUE,
            self.button_font,
            (100, 50),
            (WIDTH_MIDPOINT + 375, HEIGHT_MIDPOINT + 75),
        )

        self.algo_buttons_arr = [
            self.bubble_button,
            self.selection_button,
            self.insertion_button,
            self.shell_button,
            self.heap_button,
            self.merge_button,
            self.quick_button,
        ]
        self.chosen_algo = None
        self.sort_generator = None
        self.chosen_algo_txt = self.gui_font.render(f"Algorithm: {self.chosen_algo}", True, WHITE)
        self.chosen_algo_txt_rect = self.chosen_algo_txt.get_rect(center=(WIDTH_MIDPOINT + 375, HEIGHT_MIDPOINT + 150))

        # Conditionals
        self.img_added = False
        self.selected_grid_size = False
        self.shuffle_triggered = False
        self.sorting = False
        self.sorted = True

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
            row_and_col_val = self.grid_slider.get_value()
            self.grid = Grid(GRID_WIDTH, GRID_HEIGHT, row_and_col_val, row_and_col_val)

        # Gridlines Transparency
        self.gridlines_switch.get_clicked()

        if self.gridlines_switch.active:
            self.grid.set_alpha_max()
        else:
            self.grid.set_alpha_min()

        
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
                            block.draw_block(self.grid.image_surface)
                            self.grid.block_objects.append(block)
                            
                        self.index_grid_pos = get_index_grid_pos(self.grid.block_objects)
                        self.img_added = True
                    else:
                        self.screen.blit(self.invalid_entry, self.invalid_entry_rect)
                except FileNotFoundError:
                    self.screen.blit(self.invalid_path, self.invalid_path_rect)

        # Choosing Algorithm
        for button in self.algo_buttons_arr:
            if self.img_added:
                button.get_clicked()
            if button.clicked and not self.sorting:
                if button == self.bubble_button:
                    self.sort_generator = bubble_sort(self.grid.block_objects)
                    self.chosen_algo = "Bubble Sort"
                elif button == self.selection_button:
                    self.sort_generator = selection_sort(self.grid.block_objects)
                    self.chosen_algo = "Selection Sort"
                elif button == self.insertion_button:
                    self.sort_generator = insertion_sort(self.grid.block_objects)
                    self.chosen_algo = "Insertion Sort"
                elif button == self.shell_button:
                    self.sort_generator = shell_sort(self.grid.block_objects)
                    self.chosen_algo = "Shell Sort"
                elif button == self.heap_button:
                    self.sort_generator = heap_sort(self.grid.block_objects)
                    self.chosen_algo = "Heap Sort"
                elif button == self.merge_button:
                    self.sort_generator = merge_sort(self.grid.block_objects, self.index_grid_pos)
                    self.chosen_algo = "Merge Sort"
                elif button == self.quick_button:
                    self.sort_generator = quick_sort(self.grid.block_objects)
                    self.chosen_algo = "Quick Sort"

                self.chosen_algo_txt = self.gui_font.render(f"Algorithm: {self.chosen_algo}", True, WHITE)
                self.chosen_algo_txt_rect = self.chosen_algo_txt.get_rect(center=(WIDTH_MIDPOINT + 375, HEIGHT_MIDPOINT + 150))

        # Shuffling Image
        if self.img_added:
            self.shuffle_button.get_clicked()

        if self.shuffle_button.clicked and not self.sorting:
            shuffle_pos(self.grid.block_objects, self.index_grid_pos)
            self.sorted = False
            self.shuffle_button.clicked = False
        

        # Sorting Image
        if self.img_added:
            self.sort_button.get_clicked()
        
        if not self.sorted and self.sort_button.clicked and self.sort_generator:
                self.sorting = True

        if self.sorting:
            try:
                next(self.sort_generator)
            except StopIteration:
                self.sorted = True
                self.sorting = False
                self.chosen_algo = None
                self.chosen_algo_txt = self.gui_font.render(f"Algorithm: {self.chosen_algo}", True, WHITE)
                self.chosen_algo_txt_rect = self.chosen_algo_txt.get_rect(center=(WIDTH_MIDPOINT + 375, HEIGHT_MIDPOINT + 150))
                

        # Updates Images on screen
        for i in self.grid.block_objects:
            i.draw_block(self.grid.image_surface)
            
        
        print(f"\nimg added: {self.img_added}\nsorted: {self.sorted}\nsorting: {self.sorting}")

        self.clock.tick(FPS)
        pygame.display.update()

    def draw(self):
        # Grid
        self.screen.fill(DARK_GRAY)
        self.screen.blit(self.grid.get_images()[0], self.grid.get_images()[1])
        self.screen.blit(self.grid.get_surface_and_rect()[0], self.grid.get_surface_and_rect()[1])
        self.screen.blit(self.options_screen, self.options_screen_rect)
        self.screen.blit(self.gridlines_switch.surface, self.gridlines_switch.surface_rect)
        pygame.draw.rect(self.screen, WHITE, self.options_screen_rect, 5)
        self.options_screen.blit(self.grid_size_txt, (285, 26))
        self.options_screen.blit(self.grid_enable_txt, (285, 75))

        # Textbox
        self.screen.blit(self.img_path.get_surface_and_rect()[0], self.img_path.get_surface_and_rect()[1],)
        self.screen.blit(self.textbox_switch.surface, self.textbox_switch.surface_rect)

        # Image shuffling and sorting
        self.screen.blit(self.box_surface, self.box_surface_rect)
        self.screen.blit(self.chosen_algo_txt, self.chosen_algo_txt_rect)
        pygame.draw.rect(self.screen, WHITE, self.box_surface_rect, 5)
        self.screen.blit(self.shuffle_button.surface, self.shuffle_button.surface_rect)
        self.screen.blit(self.sort_button.surface, self.sort_button.surface_rect)
        self.screen.blit(self.heap_button.surface, self.heap_button.surface_rect)
        self.screen.blit(self.selection_button.surface, self.selection_button.surface_rect)
        self.screen.blit(self.quick_button.surface, self.quick_button.surface_rect)
        self.screen.blit(self.merge_button.surface, self.merge_button.surface_rect)
        self.screen.blit(self.shell_button.surface, self.shell_button.surface_rect)
        self.screen.blit(self.bubble_button.surface, self.bubble_button.surface_rect)
        self.screen.blit(self.insertion_button.surface, self.insertion_button.surface_rect)

    def close(self):
        pygame.quit()
        exit()


if __name__ == "__main__":
    app = App()
    app.run()
