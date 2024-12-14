from load_csv import load
from matplotlib import pyplot as plt
import numpy as np

def main():
    # try:
        data = load('population_total.csv')
        if data.empty:
            return
        
        morocco_data = data.loc[data['country'] == 'Belgium']
        france_data = data.loc[data['country'] == 'France']
        years = data.columns[1:252].to_numpy(dtype=int)
        b_population = morocco_data.values[0][1:252]
        f_population = france_data.values[0][1:252]
        
        print(f_population)

        plt.plot(years, b_population, label='Belgium')
        plt.plot(years, f_population, label='France')
        plt.yticks(np.arange(0, 250, 20))
        plt.xticks(np.arange(1800, 2050, 40))
        plt.ylabel("Population")
        plt.xlabel("Years")
        plt.title("Population Projections")
        plt.legend()
        plt.show()
    # except Exception as e:
    #     print(f"unexpected error: {e}")

if __name__ == '__main__':
    main()