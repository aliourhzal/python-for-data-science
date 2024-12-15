from load_csv import load
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def to_number(data: pd.Series):
    value = data.values[1]

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
        ipp_1900 = ipp[['country', '2020']]
        ipp_1900 = ipp_1900.apply(to_number, axis=1)

        y_axis = ley_1900.values[:, 1]

        # test = y_axis[~np.isnan(y_axis)]
        print(type(y_axis))

        # plt.scatter(ipp_1900.columns[], )
        # test = ipp_1900.loc[ipp_1900['country'] == 'United States']
        # print(test['2020'].values[0])
        # print(type(test['2020'].values[0]))
        # print(ipp_1900)
        

    # except Exception as e:
    #     print(f"error: {e}")

if __name__ == '__main__':
    main()