from random import shuffle

import pygame

from constants import *


class Block:
    def __init__(self, img_path, row, column, width, height, value):
        self.img_path = img_path
        self.row = row
        self.column = column
        self.width = width
        self.height = height
        self.value = value
        self.img = pygame.image.load(img_path)

    # positions blocks on screen based on their x and y coords
    def draw_block(self, screen):
        x = self.column * self.width
        y = self.row * self.height
        screen.blit(self.img, (x, y))
    


# BLOCK RELATED FUNCTIONS
# returns the row and column values for each index pos.
def get_index_grid_pos(blocks_lst):
    index_grid_pos = {}
    for i, b in enumerate(blocks_lst):
        index_grid_pos[i] = (b.row, b.column)

    return index_grid_pos


# shuffles the pos of block objects and updates their row and column values.
def shuffle_pos(blocks_lst, index_grid_pos):
    shuffle(blocks_lst)
    for i, b in enumerate(blocks_lst):
        b.row, b.column = index_grid_pos[i]
        print(b.row, b.column)
