import sys


def main():
    """
        This Program takes a string and gives a precise number of characters and the number of upper letters, lower letters, punctuations, spaces and digits
    """
    upper = 0
    lower = 0
    punc = 0
    digits = 0
    spaces = 0

    try:
        if len(sys.argv) > 2:
            raise AssertionError()
        elif len(sys.argv) < 2:
            print("What is the text to count?")
            text = sys.stdin.readline()
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
            else:
                punc += 1
        print(f"The text contains {len(text)} characters:")
        print(f"{upper} upper letters")
        print(f"{lower} lower letters")
        print(f"{punc} punctuation marks")
        print(f"{spaces} spaces")
        print(f"{digits} digits")

    except AssertionError:
        print(f"AssertionError: more than one argument is provided")
    except Exception as e:
        print(f"something went wrong: {e}")

if __name__ == "__main__":
    main()