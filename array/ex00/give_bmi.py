import numpy as np

def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    h_arr = np.array(height)
    w_arr = np.array(weight)

    bmi = w_arr / (h_arr ** 2)
    return list(bmi)

def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    bmi_arr = np.array(bmi)
    limit_arr = bmi_arr > limit
    return (list(limit_arr)) 

height = [2.71, 1.15]
weight = [165.3, 38.4]

bmi = give_bmi(height, weight)
print(bmi, type(bmi))
print(apply_limit(bmi, 26))