import matplotlib.pyplot as plt
from load_csv import load

def main():
    data = load("lex.csv")
    morocco_data = data.loc[data['country'] == 'Morocco']
    print(morocco_data)
    keys = data.keys()
    x_axis = keys[1:]
    print(x_axis)
    # plt.ylabel("life expectancy")
    # plt.xlabel("Year")


if __name__ == "__main__":
    main()