import pygame
from clipboard import paste
from sys import exit
from constants import *
from algorithms.bubble_sort import bubble_sort
from algorithms.heap_sort import *
from algorithms.insertion_sort import insertion_sort
from algorithms.merge_sort import *
from algorithms.quick_sort import *
from algorithms.selection_sort import selection_sort
from algorithms.shell_sort import shell_sort
from ui_elements.switch import Switch
from ui_elements.button import Button
from ui_elements.slider import Slider
from ui_elements.textbox import TextBox
from grid import Grid
from image import ImageProcessing
from block import *



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
        self.gridlines_switch = Switch("ON", "OFF", GREEN, RED, self.button_font, (50, 25), (WIDTH_MIDPOINT + 525, 50))
        self.grid_enable_text = self.gui_font.render("Gridlines", True, WHITE)
        self.grid_enable_text_rect = self.grid_enable_text.get_rect(midright=(self.gridlines_switch.position[0] - self.gridlines_switch.size[0], self.gridlines_switch.position[1],))
        self.grid_slider = Slider((284, BARRIER_PADDING_Y - 54), (150, 25), 0.5, 2, 20)
        self.confirm_grid_button = Button("OK", GREEN, LIGHT_GREEN, self.button_font, (50, 25), (164, BARRIER_PADDING_Y - 40))

        # Image Related
        self.img = ImageProcessing()
        self.img_empty = None
        self.img_path = TextBox(25, (190, HEIGHT - BARRIER_PADDING_Y + 50), BLACK, self.gui_font)
        self.textbox_switch = Switch("ADD", "DEL", GREEN, RED, self.button_font, (50, 25), (164, HEIGHT - BARRIER_PADDING_Y + 50))


        self.invalid_entry = self.gui_font.render("Invalid File Format", True, RED)
        self.invalid_entry_rect = self.invalid_entry.get_rect(bottomleft=(139, BARRIER_PADDING_Y - 5))

        self.invalid_path = self.gui_font.render("DIRECTORY DOES NOT EXIST! | click 'DEL' and try again ", True, RED)
        self.invalid_path_rect = self.invalid_path.get_rect(bottomleft=(139, BARRIER_PADDING_Y - 5))


        # Shuffling and Sorting Image
        self.box_surface = pygame.Surface((400, 250))
        self.box_surface_rect = self.box_surface.get_rect(center=(WIDTH_MIDPOINT + 375, HEIGHT_MIDPOINT ))
        self.box_surface.fill(BLACK)

        self.index_grid_pos = None
        self.shuffle_button = Button("SHUFFLE", GREEN, LIGHT_GREEN, self.button_font, (100, 50), (WIDTH_MIDPOINT + 250, HEIGHT_MIDPOINT + 75))
        self.sort_button = Button("SORT", GREEN, LIGHT_GREEN, self.button_font, (100, 50), (WIDTH_MIDPOINT + 500, HEIGHT_MIDPOINT + 75))

        self.heap_button = Button("Heap", DARK_BLUE, LIGHT_BLUE, self.button_font, (100, 50), (WIDTH_MIDPOINT + 375, HEIGHT_MIDPOINT ))
        self.selection_button = Button("Selection", DARK_BLUE, LIGHT_BLUE, self.button_font, (100, 50), (WIDTH_MIDPOINT + 375, HEIGHT_MIDPOINT - 75 ))
        self.quick_button = Button("Quick", DARK_BLUE, LIGHT_BLUE, self.button_font, (100, 50), (WIDTH_MIDPOINT + 375, HEIGHT_MIDPOINT + 75 ))

        self.merge_button = Button("Merge", DARK_BLUE, LIGHT_BLUE, self.button_font, (100, 50), (WIDTH_MIDPOINT + 500, HEIGHT_MIDPOINT ))
        self.insertion_button = Button("Insertion", DARK_BLUE, LIGHT_BLUE, self.button_font, (100, 50), (WIDTH_MIDPOINT + 500, HEIGHT_MIDPOINT -75))
        self.shell_button = Button("Shell", DARK_BLUE, LIGHT_BLUE, self.button_font, (100, 50), (WIDTH_MIDPOINT + 250, HEIGHT_MIDPOINT ))
        self.bubble_button = Button("Bubble", DARK_BLUE, LIGHT_BLUE, self.button_font, (100, 50), (WIDTH_MIDPOINT + 250, HEIGHT_MIDPOINT - 75))


        # Conditionals
        self.selected_grid_size = False
        self.added_image = False
        self.shuffled = False
        self.sorting = False
        self.sorted = False


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

        self.grid_slider.render(self.screen)
        self.grid_slider.move_slider()
        row_col_val = self.grid_slider.get_value()

        # Grid Setup
        self.confirm_grid_button.get_clicked()

        if not self.selected_grid_size:
            if self.confirm_grid_button.clicked:
                self.selected_grid_size = True
            else:
                self.grid = Grid(GRID_WIDTH, GRID_HEIGHT, row_col_val, row_col_val)

        # Gridlines Transparency
        self.gridlines_switch.get_clicked()

        if self.gridlines_switch.active:
            self.grid.set_alpha_max()
        else:
            self.grid.set_alpha_min()

        # Loading Image
        self.textbox_switch.get_clicked()

        if self.textbox_switch.active:
            self.img_path.set_text(paste())
            self.img_empty = True
            self.grid.block_objects.clear()
        else:
            if self.img_empty:
                try:
                    if self.img.verify_extension(r"{}".format(paste())):
                        self.img.update_img(paste())
                        self.img.split_into_blocks(self.grid.rows, self.grid.columns, self.grid.row_spacing, self.grid.column_spacing)

                        for i in self.img.blocks:
                            block = Block(i[0],i[1],i[2], self.grid.row_spacing, self.grid.column_spacing, i[3])
                            block.draw_block(self.grid.image_surface)
                            self.grid.block_objects.append(block)

                        self.index_grid_pos = get_index_grid_pos(self.grid.block_objects)
                        self.img_empty = False
                    else:
                        self.screen.blit(self.invalid_entry, self.invalid_entry_rect)
                except FileNotFoundError:
                    self.screen.blit(self.invalid_path, self.invalid_path_rect)
        
        # Shuffling Image
        self.shuffle_button.get_clicked()

        if not self.shuffled:
            if self.shuffle_button.clicked:
                self.shuffled = False
            else:
                shuffle_pos(self.grid.block_objects, self.index_grid_pos)
                self.shuffled = True
        
        if self.shuffle_button.clicked and self.shuffled:
            self.shuffled = False
        
        
        # Sorting Image
        self.sort_button.get_clicked()

        if not self.sorted:
            if self.sort_button.clicked:
                self.sorting = True
                print(self.index_grid_pos)
                self.sort_generator = shell_sort(self.grid.block_objects)
        
        if self.sorting:
            try:
                print("sorting")
                next(self.sort_generator)
            except StopIteration:
                self.sorted = True
                self.sorting = False
                for i in self.grid.block_objects:
                    print(f"\nvalue: {i.value}\nrow: {i.row}\ncolumn: {i.column}")
                del self.sort_generator
        
        
        if self.sort_button.clicked and self.sorted:
            self.sorted = False

        # Updating images on screen
        for i in self.grid.block_objects:
             i.draw_block(self.grid.image_surface)
        


        self.clock.tick(FPS)
        pygame.display.update()

    def draw(self):
        # Grid
        self.screen.fill(DARK_GRAY)
        self.screen.blit(self.grid.get_images()[0], self.grid.get_images()[1])
        self.screen.blit(self.grid.get_surface_and_rect()[0], self.grid.get_surface_and_rect()[1])
        self.screen.blit(self.grid_enable_text, self.grid_enable_text_rect)
        self.screen.blit(self.gridlines_switch.surface, self.gridlines_switch.surface_rect)
        self.screen.blit(self.confirm_grid_button.surface, self.confirm_grid_button.surface_rect)

        # Textbox
        self.screen.blit(self.img_path.get_surface_and_rect()[0],self.img_path.get_surface_and_rect()[1],)
        self.screen.blit(self.textbox_switch.surface, self.textbox_switch.surface_rect)

        # Image shuffling and sorting
        self.screen.blit(self.box_surface, self.box_surface_rect)
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
