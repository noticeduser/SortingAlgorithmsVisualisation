import datetime
import os
import shutil

from PIL import Image

from constants import *


class ImageProcessing:
    def __init__(self):
        self.img = None
        self.img_path = None
        self.img_name = None
        self.img_size = None
        self.return_path = None
        self.block_images = []

    # Image Processing Methods
    def subdivide_img(self, num_rows, num_columns, row_spacing, column_spacing):
        os.mkdir(self.return_path)
        if self.img_size != GRID_DIMENSIONS:
            self.crop_image()

        value = 0
        for row in range(num_rows):
            for col in range(num_columns):
                left = col * row_spacing
                upper = row * column_spacing
                right = left + row_spacing
                lower = upper + column_spacing

                block_img = self.img.crop((left, upper, right, lower))
                block_path = f"{self.return_path}/block_{row}_{col}.png"
                block_img.save(block_path)
                self.block_images.append((block_path, row, col, value))
                value += 1
                

    def crop_image(self):
        self.img = self.img.resize((GRID_WIDTH, GRID_HEIGHT))
        self.img_size = self.img.size

    # Utility Methods
    def format_path(self, path):
        path_raw_str = r"{}".format(path)
        formatted_path = path_raw_str.replace("\\", "/")
        return formatted_path

    def verify_extension(self, path):
        if len(path) == 0:
            return False
        path = self.check_quotations(path)
        extension = os.path.splitext(path)[1]
        if extension not in [".jpg", ".jpeg", ".png"]:
            return False
        return True

    def check_quotations(self, path):
        if path[0] == '"':
            path = path.replace('"', "")
        return path

    def get_time(self):
        current_datetime = datetime.datetime.now()
        formatted_datetime = current_datetime.strftime("%Y%m%d_%H%M%S")
        return formatted_datetime

    def del_images(self):
        folders = os.listdir("images/user_images/")
        for folder in folders:
            folder_path = os.path.join("images/user_images/", folder)
            shutil.rmtree(folder_path)

    # Image Loading and Updating Methods
    def update_img(self, path):
        path = self.check_quotations(path)
        self.img_path = self.format_path(path)
        self.img = Image.open(self.img_path)
        self.img_name = os.path.basename(path)[:-4]
        self.return_path = f"images/user_images/{self.img_name}_{self.get_time()}"
        self.img_size = self.img.size
        self.block_images.clear()
