from load_csv import load
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def to_number(data: pd.Series):
    value = data.values[1]

    if isinstance(value, int):
        return data

    if value.isalpha():
        return data

    if value[-1].isdigit():
         data.values[1] = int(value)
    else:
        data.values[1] = int(float(value[:-1]) * 1e3)
    return data

def main():
    # try:
        ley = load('life_expectancy_years.csv')
        ipp = load('income_per_person_gdppercapita_ppp_inflation_adjusted.csv')

        if ley.empty or ipp.empty:
            return
        ley_1900 = ley[['country', '1900']]
        ipp_1900 = ipp[['country', '1900']]

        ipp_1900 = ipp_1900.apply(to_number, axis=1)
        ley_1900 = ley_1900[~np.isnan(ley_1900['1900'])]
        
        ipp_1900 = ipp_1900[ipp_1900['country'].isin(ley_1900['country'])]

        plt.scatter(ipp_1900['1900'].values, ley_1900['1900'].values)
        plt.xscale('log')
        plt.xticks([300, 1000, 10000], labels=['300', '1k', '10k'])
        plt.xlabel('Gross domestic product')
        plt.ylabel('Life Expectancy')
        plt.title('1900')
        plt.show()
        

    # except Exception as e:
    #     print(f"error: {e}")

if __name__ == '__main__':
    main()