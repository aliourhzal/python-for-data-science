import numpy as np

def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    h_arr = np.array(height)
    w_arr = np.array(weight)

    bmi = w_arr / (h_arr ** 2)
    return list(bmi)

height = [2.71, 1.15]
weight = [165.3, 38.4]

bmi = give_bmi(height, weight)
print(bmi, type(bmi))