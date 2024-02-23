from math import floor

import pygame

from constants import *


class Grid:
    def __init__(self, width, height, rows, columns):
        self.width = width
        self.height = height
        self.rows = rows
        self.columns = columns
        self.column_spacing, self.row_spacing = self.set_row_column_spacing()
        self.block_size = self.row_spacing * self.column_spacing
        self.gridlines_surface = self.draw_gridlines()
        self.image_surface = pygame.Surface((width, height), pygame.SRCALPHA)
        self.block_objects = []


    def set_row_column_spacing(self):
        row_spacing = round(self.height / self.rows)
        column_spacing = round(self.width / self.columns)

        return (row_spacing, column_spacing)

    def draw_gridlines(self):
        grid_surface = pygame.Surface((self.width + 2, self.height + 2), pygame.SRCALPHA)

        row_spacing = self.height / self.rows
        column_spacing = self.width / self.columns
        print(f"block size: {row_spacing * column_spacing}")

        start_pos_rows = 0
        start_pos_columns = 0

        for _ in range(self.rows + 1):
            pygame.draw.line(
                surface=grid_surface,
                color=WHITE,
                width=3,
                start_pos=(0, start_pos_rows),
                end_pos=(self.width, start_pos_rows),
            )
            start_pos_rows += row_spacing

        for _ in range(self.columns + 1):
            pygame.draw.line(
                surface=grid_surface,
                color=WHITE,
                width=3,
                start_pos=(start_pos_columns, 0),
                end_pos=(start_pos_columns, self.height),
            )
            start_pos_columns += column_spacing

        return grid_surface

    def get_surface_and_rect(self):
        return (
            self.gridlines_surface,
            self.gridlines_surface.get_rect(center=(WIDTH_MIDPOINT, HEIGHT_MIDPOINT)),
        )

    def get_images(self):
        return (
            self.image_surface,
            self.image_surface.get_rect(center=(WIDTH_MIDPOINT, HEIGHT_MIDPOINT)),
        )

    # Handles the transparency of the gridlines
    def set_alpha_min(self):
        return self.gridlines_surface.set_alpha(0)

    def set_alpha_max(self):
        return self.gridlines_surface.set_alpha(255)
