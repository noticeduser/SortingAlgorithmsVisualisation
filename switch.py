import pygame
from constants import *

class Switch:
    def __init__(self, primary_text, secondary_text, primary_colour, secondary_colour, font, size, position):
        # Core attributes
        self.position = position
        self.size = size

        # Surface setup
        self.surface = pygame.Surface(size)
        self.surface_rect = self.surface.get_rect(center=position)

        # Text
        text_size = (size[0] // 2, size[1] // 2)

        self.primary_text = font.render(primary_text, True, WHITE)
        self.primary_text_rect = self.primary_text.get_rect(center= text_size)

        self.secondary_text = font.render(secondary_text, True, WHITE)
        self.secondary_text_rect = self.secondary_text.get_rect(center=text_size)

        # Colours
        self.primary_colour = primary_colour
        self.secondary_colour = secondary_colour

        # Setup
        self.surface.fill(primary_colour)
        self.surface.blit(self.primary_text, self.primary_text_rect)

        # Boolean Values
        self.active = True
        self.pressed = False
        

    def get_clicked(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.surface_rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0]:
                self.pressed = True
            else:
                if self.pressed == True:
                    if self.active:
                        self.set_secondary()
                    else:
                        self.set_primary()

    def set_primary(self):
        self.surface.fill(self.primary_colour)
        self.surface.blit(self.primary_text, self.primary_text_rect)
        self.active = True
        self.pressed = False

    def set_secondary(self):
        self.surface.fill(self.secondary_colour)
        self.surface.blit(self.secondary_text, self.secondary_text_rect)
        self.active = False
        self.pressed = False
