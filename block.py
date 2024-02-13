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


# def shuffle_pos(blocks_lst):
#     positions = [(block.original_row, block.original_column) for block in blocks_lst]
#     random.shuffle(positions)

#     for block, (new_row, new_column) in zip(blocks_lst, positions):
#         block.row = new_row
#         block.column = new_column

#     for i in blocks_lst:
#            for j in blocks_lst:
#                   if i.row == j.original_row and i.column == j.original_column:
#                          i.value = j.value

#     return blocks_lst

def shuffle_pos(blocks_lst):
    positions = [(block.original_row, block.original_column) for block in blocks_lst]
    random.shuffle(positions)

    for block, (new_row, new_column) in zip(blocks_lst, positions):
        block.row = new_row
        block.column = new_column
        # Update the block's value to the value associated with its new position
        for other_block in blocks_lst:
            if other_block.row == new_row and other_block.column == new_column:
                block.value = other_block.value
                break  # Once we find the matching block, no need to continue searching

    return blocks_lst


def shuffle_pos(blocks_lst):

    index_gridpos = {}
    for i, b in enumerate(blocks_lst):
        index_gridpos[i] = (b.original_row, b.original_column)

    random.shuffle(blocks_lst)
    
    for i, b in enumerate(blocks_lst):
        b.row, b.column = index_gridpos[i]
          
          
          
        