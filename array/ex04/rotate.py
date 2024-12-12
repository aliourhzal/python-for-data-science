from PIL import Image
from load_image import ft_load
import numpy as np

def transpose(arr: np.array) -> np.array:
    new_arr = np.array([])
    cols = arr.shape[1]

    for i in range(cols):
        new_row = arr[:, i]
        if i == 0:
            new_arr = np.array([new_row.tolist()])
        else:
            new_arr = np.vstack([new_arr, new_row])
    
    return new_arr

def main():
    start_x = 100
    start_y = 450
    img = ft_load('animal.jpeg')
    if not len(img):
        return
    
    zoom = img[start_x:start_x + 400, start_y:start_y + 400, 0:1]
    zoom_2d = zoom[:, :, 0]
    # print(f"The shape of image is: {zoom.shape} or {(zoom_2d.shape)}")
    transposed_arr = transpose(zoom_2d)
    # print(f"The shape of image is: {transposed_arr.shape}")
    # print(transposed_arr)
    transposed_img = Image.fromarray(transposed_arr.astype("uint8"))
    transposed_img.save("rotate.jpeg")


if __name__ == "__main__":
    main()