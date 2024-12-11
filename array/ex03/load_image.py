import numpy as np
from PIL import Image


def ft_load(path: str) -> np.array:
    try:
        if not path.endswith(".jpg") and not path.endswith(".jpeg"):
            raise AssertionError("the provided file is not jpg nor jpeg")
        img = Image.open(path)
        img_arr = np.array(img)
        print(f"The shape of image is: {img_arr.shape}")
        return img_arr
    except AssertionError as e:
        print(f"AssertionError: {str(e)}")
        return np.array([])
    except Exception as e:
        print(f"error: {str(e)}")
        return np.array([])


