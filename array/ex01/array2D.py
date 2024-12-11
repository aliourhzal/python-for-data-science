import numpy as np

def check_args(family: list, start: int, end: int) -> bool:
    if not isinstance(family, list):
        return False
    if not isinstance(start, int) or not isinstance(end, int):
        return False
    return True

def slice_me(family: list, start: int, end: int) -> list:
    try:
        np.warnings.filterwarnings('error', category=np.VisibleDeprecationWarning)
        if not check_args(family, start, end):
            return
        family_arr = np.array(family)
        print(f"My shape is : {family_arr.shape}")
        new_family = family_arr[start:end]
        print(f"My new shape is : {new_family.shape}")
        return (new_family.tolist())

    except Exception as e:
        if isinstance(e, np.VisibleDeprecationWarning):
            print("the provided lists are not the same size")
        print(f"unexpected error: {e}")
        return []
