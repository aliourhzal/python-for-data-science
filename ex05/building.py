import sys


def main():
    upper = 0
    lower = 0
    punc = 0
    digits = 0
    spaces = 0

    try:
        if len(sys.argv) > 2:
            raise AssertionError()
        elif len(sys.argv) < 2:
            text = input("What is the text to count?\n")
        else:
            text = sys.argv[1]

        for c in text:
            if c.isupper():
                upper += 1
            elif c.islower():
                lower += 1
            elif c.isdigit():
                digits += 1
            elif c.isspace():
                spaces += 1

    except AssertionError:
        print(f"AssertionError: more than one argument is provided")

if __name__ == "__main__":
    main()