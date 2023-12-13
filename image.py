import pygame
from PIL import Image
from clipboard import paste
import os

def format_path(path):
    path_raw_str = r"{}".format(path)
    formatted_path = path_raw_str.replace("\\", "/")
    return formatted_path

def verify_extension(path):
    extension = os.path.splitext(path)[1]
    print(extension)
    if extension not in [".jpg", ".png"]:
        return False
    return True


class ImageProcessing:
    def __init__(self, img_path):
        self.img_path = img_path
        self.img = Image.open(img_path)
        self.img_name = os.path.basename(img_path)[:-4]
        # self.img_size = self.img.PIL.size()
        self.return_path = f"images/user_images/{self.img_name}"


# image_object = ImageProcessing("C:/Users/Culle/Desktop/assets/joey.jpg")
# print(image_object.return_path)


class ImageProcessing:
    def __init__(self):
        self.img_path = None

    def set_img_path(self, path):
        self.img_path = path
