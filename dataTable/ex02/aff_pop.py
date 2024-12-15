from load_csv import load
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np

def to_number(data: pd.Series):
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
        
        morocco_data = data.loc[data['country'] == 'Morocco']
        france_data = data.loc[data['country'] == 'France']
        france_data = france_data.apply(to_number, axis=0)
        morocco_data = morocco_data.apply(to_number, axis=0)
        years = data.columns[1:252].to_numpy(dtype=int)
        b_population = morocco_data.values[0][1:252]
        f_population = france_data.values[0][1:252]

        plt.plot(years, b_population, label='Morocco', color='r')
        plt.plot(years, f_population, label='France', color='k')
        plt.yticks(np.arange(20*1e6,80*1e6, 20*1e6), ['20M', '40M', '60M'])
        plt.xticks(np.arange(1800, 2050, 40))
        plt.ylabel("Population")
        plt.xlabel("Years")
        plt.title("Population Projections")
        plt.legend(loc=4)
        plt.show()
    # except Exception as e:
    #     print(f"unexpected error: {e}")

if __name__ == '__main__':
    main()