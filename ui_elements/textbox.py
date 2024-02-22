import pygame

from constants import *


class TextBox:
    def __init__(self, height, position, colour, font):
        # attributes relating to appearance
        self.height = height
        self.position = position
        self.colour = colour
        self.font = font

        # attributes relating to text
        self.text = ""
        self.text_surf = None
        self.text_rect = None
        self.text_width = None

        # initializing surface
        self.surface = None

    def create_box(self):
        box_surface = pygame.Surface((self.text_width + 10, self.height))
        box_surface.fill(self.colour)
        box_surface.blit(self.text_surf, self.text_rect)
        return box_surface

    def set_text(self, new_text):
        self.text = new_text
        self.update_text_surf()

    def clear_text(self):
        self.text = ""
        self.update_text_surf()

    def update_text_surf(self):
        self.text_surf = self.font.render(self.text, True, WHITE)
        self.text_rect = self.text_surf.get_rect(midleft=(5, self.height // 2))
        self.text_width = self.text_surf.get_size()[0]
        self.surface = self.create_box()

    def get_text(self):
        return self.text

    def get_surface_and_rect(self):
        return (self.surface, self.surface.get_rect(midleft=self.position))
