
import numpy as np
from numpy import array
from PIL import Image

def ft_invert(array) -> array:
    """Inverts the color of the image received."""
    if not len(array):
        return array([])
    inverted = 255 - array
    img = Image.fromarray(inverted)
    img.save("inverted.jpg")
    return inverted

def ft_red(array) -> array:
    """Keep only the red channel of the color of the image received."""
    if not len(array):
        return array([])
    zero_arr = np.zeros_like(array)
    zero_arr[:, :, 0] = array[:, :, 0]
    img = Image.fromarray(zero_arr)
    img.save("red.jpg")
    return (zero_arr)



def ft_green(array) -> array:
    """Keep only the green channel of the color of the image received."""
    if not len(array):
        return array([])
    zero_arr = np.zeros_like(array)
    zero_arr[:, :, 1] = array[:, :, 1]
    img = Image.fromarray(zero_arr)
    img.save("green.jpg")
    return (zero_arr)

def ft_blue(array) -> array:
    """Keep only the blue channel of the color of the image received."""
    if not len(array):
        return array([])
    zero_arr = np.zeros_like(array)
    zero_arr[:, :, 2] = array[:, :, 2]
    img = Image.fromarray(zero_arr)
    img.save("blue.jpg")
    return (zero_arr)

def ft_grey(array) -> array:
    """Makes the received image gray"""
    if not len(array):
        return array([])
    gray_arr = array[:, :, 1]
    img = Image.fromarray(gray_arr)
    img.save("gray.jpg")
    return (gray_arr)
