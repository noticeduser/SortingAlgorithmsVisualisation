import pygame

from constants import *


class Button:
    def __init__(self, text, colour, hover_colour, font, size, position):
        # Core attributes
        self.position = position
        self.size = size

        # Surface setup
        self.surface = pygame.Surface(size)
        self.surface_rect = self.surface.get_rect(center=position)

        # Text
        text_size = (size[0] // 2, size[1] // 2)
        self.text_rendered = font.render(text, True, WHITE)
        self.text_rect = self.text_rendered.get_rect(center=text_size)

        # Colour
        self.colour = colour
        self.hover_colour = hover_colour
        self.hovering = False

        # Setup
        self.surface.fill(colour)
        self.surface.blit(self.text_rendered, self.text_rect)

        # Action
        self.clicked = False

    def get_clicked(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.surface_rect.collidepoint(mouse_pos):
            if not self.hovering:
                self.update_colour(self.hover_colour)
                self.hovering = True
            if pygame.mouse.get_pressed()[0]:
                self.clicked = True
            else:
                if self.clicked:
                    self.clicked = False
        else:
            if self.hovering:
                self.update_colour(self.colour)
                self.hovering = False

    def update_colour(self, colour):
        self.surface.fill(colour)
        self.surface.blit(self.text_rendered, self.text_rect)
