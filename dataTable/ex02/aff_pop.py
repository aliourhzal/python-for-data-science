from load_csv import load
from matplotlib import pyplot as plt
import pandas as pn
import numpy as np

def to_number(data: pn.Series):
    value = data.values[0]

    if value[0].isalpha():
        return data
    
    if value[-1].isdigit():
         return int(value)

    last_letter = value[-1].upper()

    if last_letter == 'K':
        return int(float(value[:-1]) * 1e3)        
    elif last_letter == 'M':
        return int(float(value[:-1]) * 1e6)
    elif last_letter == 'B':
        return int(float(value[:-1]) * 1e9)

def main():
    # try:
        data = load('population_total.csv')
        if data.empty:
            return
        
        belgium_data = data.loc[data['country'] == 'Belgium']
        france_data = data.loc[data['country'] == 'France']
        france_data = france_data.apply(to_number, axis=0)
        belgium_data = belgium_data.apply(to_number, axis=0)
        years = data.columns[1:252].to_numpy(dtype=int)
        b_population = belgium_data.values[0][1:252]
        f_population = france_data.values[0][1:252]

        # plt.plot(years, b_population, label='Belgium')
        # plt.plot(years, f_population, label='France')
        # plt.yticks(np.arange(0, 250, 20))
        # plt.xticks(np.arange(1800, 2050, 40))
        # plt.ylabel("Population")
        # plt.xlabel("Years")
        # plt.title("Population Projections")
        # plt.legend(loc=4)
        # plt.show()
    # except Exception as e:
    #     print(f"unexpected error: {e}")

if __name__ == '__main__':
    main()