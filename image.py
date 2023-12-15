from PIL import Image
import os
from constants import *


class ImageProcessing:
    def __init__(self):
        self.img = None
        self.img_path = None
        self.img_name = None
        self.img_size = None
        self.return_path = None

    def split_into_blocks(self, num_rows, num_columns, row_spacing, column_spacing):
            os.mkdir(self.return_path)
            if self.img_size != GRID_DIMENSIONS:
                self.crop_image()
            
            for row in range(num_rows):
                for col in range(num_columns):
                    left = col * row_spacing
                    upper = row * column_spacing
                    right = left + row_spacing
                    lower = upper + column_spacing
            
                    block = self.img.crop((left, upper, right, lower))
                    print("{self.return_path}/block_{row}_{col}.png")
                    block.save(f"{self.return_path}/block_{row}_{col}.png")

    def format_path(self, path):
        path_raw_str = r"{}".format(path)
        formatted_path = path_raw_str.replace("\\", "/")
        return formatted_path

    def verify_extension(self, path):
        path = self.check_quotations(path)

        extension = os.path.splitext(path)[1]
        if extension not in [".jpg", ".png"]:
            return False
        return True

    def check_quotations(self, path):
        if path[0] == '"':
            path = path.replace('"', "")
        return path

    def crop_image(self):
        self.img = self.img.resize((GRID_WIDTH, GRID_HEIGHT))
        self.img_size = self.img.size

    def update_img(self, path):
        path = self.check_quotations(path)
        self.img_path = self.format_path(path)
        self.img = Image.open(self.img_path)
        self.img_name = os.path.basename(path)[:-4]
        self.return_path = f"images/user_images/{self.img_name}"
        self.img_size = self.img.size
        print('run')


# testimage = ImageProcessing()
# testimage.update_img(r"C:\Users\notic\OneDrive\Desktop\scp.jpg")
# testimage.split_into_blocks(10, 10, 50, 50)