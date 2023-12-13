import pygame
from constants import *


class Block:
    def __init__(
        self,
        block_width,
        block_height,
        block_size,
        image,
        coords_original,
        pos_original,
    ):
        self.block_width = block_width
        self.block_height = block_height
        self.block_size = block_size
        self.image = image

        self.coords_original = coords_original
        self.pos_original = pos_original

        self.coords_current = self.coords_original
        self.pos_current = self.pos_original

    def draw_block(self):
        block_surface = pygame.Surface((self.block_width, self.block_height))
        block_surface.blit(self.image)

    def set_pos_current(self, pos):
        self.pos_current = pos

    def set_coords_current(self, coords):
        self.coords_current = coords
