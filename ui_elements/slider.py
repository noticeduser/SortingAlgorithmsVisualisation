import pygame
from math import floor
from constants import *


class Slider:
    def __init__(self, pos, size, initial_val, min_val, max_val) -> None:
        self.pos = pos
        self.size = size

        self.slider_left_pos = self.pos[0] - (size[0] // 2)
        self.slider_right_pos = self.pos[0] + (size[0] // 2)
        self.slider_top_pos = self.pos[1] - (size[1] // 2)

        self.min_val = min_val
        self.max_val = max_val
        self.initial_val = (self.slider_right_pos - self.slider_left_pos) * initial_val

        self.containter_rect = pygame.Rect(
            self.slider_left_pos, self.slider_top_pos, self.size[0], self.size[1]
        )
        self.button_rect = pygame.Rect(
            self.slider_left_pos + self.initial_val - 5,
            self.slider_top_pos,
            10,
            self.size[1],
        )

        self.pressed = False

    def move_slider(self):
        mouse_pos = pygame.mouse.get_pos()
        mouse = pygame.mouse.get_pressed()

        if self.containter_rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0] and mouse[0]:
                self.button_rect.centerx = mouse_pos[0]

    def get_value(self):
        val_range = self.slider_right_pos - self.slider_left_pos - 2
        button_val = self.button_rect.centerx - self.slider_left_pos

        return floor(
            (button_val / val_range) * (self.max_val - self.min_val) + self.min_val
        )

    def render(self, screen):
        pygame.draw.rect(screen, LIGHT_GRAY, self.containter_rect)
        pygame.draw.rect(screen, RED, self.button_rect)
