import pygame
import random
from constants import *

class Block:
    def __init__(self, img_path, row, column, width, height, value):
            self.img_path = img_path
            self.row = row
            self.column = column
            self.original_row = row
            self.original_column = column
            self.width = width
            self.height = height
            self.value = value
            self.img = pygame.image.load(img_path)

    def set_block(self, img_path, row, column, width, height, value):
                self.img_path = img_path
                self.row = row
                self.column = column
                self.original_row = row
                self.original_column = column
                self.width = width
                self.height = height
                self.value = value
                self.img = pygame.image.load(img_path)
          
    
    def draw_block(self, screen):
           x = self.column * self.width
           y = self.row * self.height
           screen.blit(self.img, (x, y))


def shuffle_pos(blocks_lst):
    positions = [(block.original_row, block.original_column) for block in blocks_lst]
    random.shuffle(positions)

    for block, (new_row, new_column) in zip(blocks_lst, positions):
        block.row = new_row
        block.column = new_column

    return blocks_lst
