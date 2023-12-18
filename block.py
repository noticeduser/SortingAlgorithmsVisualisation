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

       rows_lst = []
       columns_lst = []
       index_pos = 0

       for block in blocks_lst:
              rows_lst.append(block.original_row)
              columns_lst.append(block.original_column)
              
       random.shuffle(rows_lst)
       random.shuffle(columns_lst)



       for block in blocks_lst:
              block.row = rows_lst[index_pos]
              block.column = columns_lst[index_pos]
              index_pos += 1
       
       return blocks_lst