import numpy as np

def check_args(height: any, weight: any) -> bool:
    if not isinstance(height, list) or not isinstance(weight,list):
        return False
    if len(height) != len(weight):
        return False
    valid_heights = all([(isinstance(item, int) or isinstance(item, float)) for item in height])
    if not valid_heights:
        return False
    valid_weights = all([(isinstance(item, int) or isinstance(item, float)) for item in weight])
    if not valid_weights:
        return False
    
    return True

def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    if not check_args(height=height, weight=weight):
        return []
    h_arr = np.array(height)
    w_arr = np.array(weight)

    bmi = w_arr / (h_arr ** 2)
    return list(bmi)

def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    bmi_arr = np.array(bmi)
    limit_arr = bmi_arr > limit
    return (list(limit_arr)) 