import pygame
from clipboard import paste
from sys import exit
from constants import *
from switch import Switch
from grid import Grid
from textbox import TextBox
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

        # Grid intialized
        self.grid = Grid(GRID_WIDTH, GRID_HEIGHT, 5, 5)
        self.gridlines_switch = Switch(
            "ON", "OFF", GREEN, RED, self.button_font, (50, 25), (WIDTH - 100, 50)
        )
        self.grid_enable_text = self.gui_font.render("GRIDLINES", True, WHITE)
        self.grid_enable_text_rect = self.grid_enable_text.get_rect(
            midright=(
                self.gridlines_switch.position[0] - self.gridlines_switch.size[0],
                self.gridlines_switch.position[1],
            )
        )

        # Image Initialized
        self.img = ImageProcessing()
        self.img_empty = None
        self.img_path = TextBox(25, (BARRIER_PADDING_X + 50, 50), BLACK, self.gui_font)
        self.textbox_switch = Switch(
            "ADD",
            "DEL",
            GREEN,
            RED,
            self.button_font,
            (50, 25),
            (BARRIER_PADDING_X + 25, 50),
        )

        self.added_text = self.gui_font.render("IMAGE ADDED", True, GREEN)
        self.added_text_rect = self.added_text.get_rect(
            bottomleft=(BARRIER_PADDING_X, BARRIER_PADDING_Y - 10)
        )

        self.not_added = self.gui_font.render("IMAGE NOT ADDED", True, RED)
        self.not_added_rect = self.not_added.get_rect(
            bottomleft=(BARRIER_PADDING_X, BARRIER_PADDING_Y - 10)
        )

        self.invalid_entry = self.gui_font.render("Invalid File Format", True, RED)
        self.invalid_entry_rect = self.invalid_entry.get_rect(
            bottomleft=(BARRIER_PADDING_X, BARRIER_PADDING_Y - 85)
        )

        self.invalid_path = self.gui_font.render("DIRECTORY DOES NOT EXIST! | click 'DEL' and try again ", True, RED)
        self.invalid_path_rect = self.invalid_path.get_rect(
            bottomleft=(BARRIER_PADDING_X, BARRIER_PADDING_Y - 85)
        )

        # Shuffling Image
        self.shuffled = False
        self.shuffle_switch = Switch("Shuffle", "Sort", GREEN, RED, self.button_font, (50, 25), (WIDTH - 100, 100))

    def run(self):
        while self.running:
            self.update()
            self.draw()
        self.close()

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

        # Gridlines Transparency
        self.gridlines_switch.get_clicked()

        if self.gridlines_switch.active:
            self.grid.set_alpha_max()
        else:
            self.grid.set_alpha_min()

        # Loading Image
        self.textbox_switch.get_clicked()

        if self.img_empty:
            self.screen.blit(self.not_added, self.not_added_rect)
        else:
            self.screen.blit(self.added_text, self.added_text_rect)

        if self.textbox_switch.active:
            self.img_path.set_text(paste())
            self.img_empty = True
        else:
            if self.img_empty:
                try:
                    if self.img.verify_extension(r"{}".format(paste())):
                        self.img.update_img(paste())
                        self.img.split_into_blocks(self.grid.rows, self.grid.columns, self.grid.row_spacing, self.grid.column_spacing)
                        for i in self.img.blocks:
                            block = Block(i[0],i[1],i[2], self.grid.row_spacing, self.grid.column_spacing, i[3])
                            #block.draw_block(self.grid.image_surface)
                            self.grid.block_objects.append(block)

                        self.img_empty = False
                    else:
                        self.screen.blit(self.invalid_entry, self.invalid_entry_rect)
                except FileNotFoundError:
                    self.screen.blit(self.invalid_path, self.invalid_path_rect)
        
        # Shuffling Image
        self.shuffle_switch.get_clicked()

        if self.shuffled == False:
            if self.shuffle_switch.active:
                pass
            else:
                shuffle_pos(self.grid.block_objects)
                self.shuffled = True

        self.clock.tick(FPS)
        pygame.display.update()

    def draw(self):
        # Grid
        self.screen.fill(DARK_GRAY)
        self.screen.blit(
            self.grid.get_images()[0], self.grid.get_images()[1]
        )
        self.screen.blit(
            self.grid.get_surface_and_rect()[0], self.grid.get_surface_and_rect()[1]
        )
        self.screen.blit(self.grid_enable_text, self.grid_enable_text_rect)
        self.screen.blit(
            self.gridlines_switch.surface, self.gridlines_switch.surface_rect
        )

        # Textbox
        self.screen.blit(
            self.img_path.get_surface_and_rect()[0],
            self.img_path.get_surface_and_rect()[1],
        )
        self.screen.blit(self.textbox_switch.surface, self.textbox_switch.surface_rect)


        # Image shuffling
        self.screen.blit(self.shuffle_switch.surface, self.shuffle_switch.surface_rect)
        for i in self.grid.block_objects:
            i.draw_block(self.grid.image_surface)
        for i in self.grid.block_objects:
            print(f"pic {i.value}\told: {i.original_row},{i.original_column}\tnew: {i.row},{i.column}")
        
    def close(self):
        pygame.quit()
        exit()


if __name__ == "__main__":
    app = App()
    app.run()
