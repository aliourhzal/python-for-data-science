from load_image import ft_load
from PIL import Image

def main():
    start_x = 100
    start_y = 450
    img_arr = ft_load("animal.jpeg")
    if not len(img_arr):
        return 
    zoom = img_arr[start_x:start_x + 400, start_y:start_y + 400, 0:1];
    print(f"New shape after slicing: {zoom.shape} or {zoom[:, :, 0].shape}")
    print(zoom)
    new_img = Image.fromarray(zoom[:, :, 0])
    new_img.save("zoom_animal.jpeg")


if __name__ == "__main__":
    main()