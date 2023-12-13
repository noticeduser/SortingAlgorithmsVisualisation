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

    
    def update_img(self, path):
        self.img_path = self.format_path(path)
        self.img = Image.open(self.img_path)
        self.img_name = os.path.basename(path)[:-4]
        self.return_path = f"images/user_images/{self.img_name}"
        self.img_size = self.img.size
        
        if self.img_size != GRID_DIMENSIONS:
            self.crop_image()

    def verify_extension(path):
        extension = os.path.splitext(path)[1]
        if extension not in [".jpg", ".png"]:
            return False
        return True
    
    def format_path(path):
        path_raw_str = r"{}".format(path)
        formatted_path = path_raw_str.replace("\\", "/")
        return formatted_path
    
    def crop_image(self):
        self.img = self.img.resize((GRID_WIDTH, GRID_HEIGHT))





# image_object = ImageProcessing("C:/Users/Culle/Desktop/assets/joey.jpg")
# print(image_object.return_path)