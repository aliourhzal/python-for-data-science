import matplotlib.pyplot as plt
from load_csv import load
import numpy as np

def main():
    try:
        data = load("life_expectancy_years.csv")
        if data.empty:
            return 
        morocco_row = data.loc[data['country'] == 'France']
        morocco_data = morocco_row.values[0][1:]
        years = morocco_row.columns[1:].to_numpy()

        plt.xticks(np.arange(0, 300, 40))
        plt.ylabel("Life expectancy")
        plt.xlabel("Year")
        plt.title("Morocco Life expectancy Projections")
        plt.plot(years, morocco_data)
        plt.show()
    except Exception as e:
        print(f"unexpected error: {e}")

if __name__ == "__main__":
    main()