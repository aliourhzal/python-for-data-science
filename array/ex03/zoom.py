from load_image import ft_load
import numpy as np
from PIL import Image

def main():
    start_x = 100
    start_y = 450
    img_arr = ft_load("animal.jpeg")
    gray_img = img_arr
    if not len(img_arr):
        return 
    print(img_arr)
    zoom = img_arr[start_x:start_x + 400, start_y:start_y + 400];
    print(f"New shape after slicing: {zoom.shape}")
    print(zoom)
    new_img = Image.fromarray(zoom)
    new_img.save("test.jpeg")
    

if __name__ == "__main__":
    main()