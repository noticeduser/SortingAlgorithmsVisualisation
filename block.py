import pygame
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
    
    def update_pos(self, new_row, new_column):
           self.row = new_row
           self.column = new_column
    
    def draw_block(self, screen):
           x = self.column * self.width
           y = self.row * self.height
           screen.blit(self.img, (x, y))
