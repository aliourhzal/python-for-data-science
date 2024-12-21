from math import sqrt


def mean(*args: any):
    return (sum(args) / len(args))

def median(*args: any):
    is_even = len(args) % 2 == 0

    sorted_args = sorted(args)
    size = len(sorted_args)

    if not is_even:
        return sorted_args[size // 2]
    else:
        min_mid = size // 2 - 1
        return (sum(sorted_args[min_mid:min_mid + 2]) / 2)
    
def quartile(*args: any):
    is_even = len(args) % 2 == 0

    sorted_args = sorted(args)
    first_quarter = sorted_args[0:len(sorted_args) // 2]
    lower_quartile = first_quarter[len(first_quarter) // 2]

    reversed_sorted = sorted(args, reverse=True)
    last_quarter = reversed_sorted[0:len(reversed_sorted) // 2]
    upper_quartile = last_quarter[len(last_quarter) // 2]

    return [float(lower_quartile), float(upper_quartile)]

def var(*args: any):
    data_mean = mean(*args)

    total_deviation = 0

    for val in args:
        total_deviation += (val - data_mean) ** 2
    return (total_deviation / len(args))

def std(*args: any):
    return sqrt(var(*args))


def ft_statistics(*args: any, **kwargs: any) -> None:

    if len(args) == 0:
        print('ERROR')
        return 

    for val in kwargs.values():
        if val == 'mean':
            print(f"mean: {mean(*args)}")
        elif val == 'median':
            print(f"median: {median(*args)}")
        elif val == 'quartile':
            print(f"quartile: {quartile(*args)}")
        elif val == 'std':
            print(f"std: {std(*args)}")
        elif val == 'var':
            print(f"var: {var(*args)}")
        else:
            print('ERROR')
    return 

ft_statistics(1, 42, 360, 11, 64, toto="mean", tutu="median", tata="quartile")
print("-----")
ft_statistics(5, 75, 450, 18, 597, 27474, 48575, hello="std", world="var")
print("-----")
ft_statistics(5, 75, 450, 18, 597, 27474, 48575, ejfhhe="heheh", ejdjdejn="kdekem")
print("-----")
ft_statistics(toto="mean", tutu="median", tata="quartile")