import pygame
from PIL import Image
import os


class ImageProcessing:
    def __init__(self, img_path) -> None:
        self.img = Image.open(img_path)
        self.img_path = img_path
        self.img_name = os.path.basename(img_path)[:-4]
        # self.img_size = self.img.PIL.size()
        self.return_path = f"images/user_images/{self.img_name}"


image_object = ImageProcessing("C:/Users/notic/OneDrive/Desktop/scp.jpg")
print(image_object.return_path)
