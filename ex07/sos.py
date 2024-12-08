import sys

NESTED_MORSE = {
    " ": "/ ",
    "A": ".- ",
    "B": "-... ",
    "C": "-.-. ",
    "D": "-.. ",
    "E": ". ",
    "F": "..-. ",
    "G": "--. ",
    "H": ".... ",
    "I": ".. ",
    "J": ".--- ",
    "K": "-.- ",
    "L": ".-.. ",
    "M": "-- ",
    "N": "-. ",
    "O": "--- ",
    "P": ".--. ",
    "Q": "--.- ",
    "R": ".-. ",
    "S": "... ",
    "T": "- ",
    "U": "..- ",
    "V": "...- ",
    "W": ".-- ",
    "X": "-..- ",
    "Y": "-.-- ",
    "Z": "--.. ",
    "0": "----- ",
    "1": ".---- ",
    "2": "..--- ",
    "3": "...-- ",
    "4": "....- ",
    "5": "..... ",
    "6": "-.... ",
    "7": "--... ",
    "8": "---.. ",
    "9": "----. "
}

def check_string(str: str):
    for c in str:
        if not c.isdigit() and not c.isalnum() and c != " ":
            return False

    return True

def main():
    try:
        args = sys.argv
        morse = ""

        if len(args) != 2 or not check_string(args[1]):
            raise AssertionError()
        for c in args[1]:
            morse += NESTED_MORSE[c.upper()]
        print(morse)
    except AssertionError:
        print("AssertionError: the arguments are bad")
    except Exception as e:
        print(f"something went wrong: {e}")

if __name__ == "__main__":
    main()