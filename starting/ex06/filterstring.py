import sys
from ft_filter import ft_filter

def check_string(str: str):
    special_chars = [c for c in str if not c.isalnum() and c != " "]
    if len(special_chars) == 0:
        return True
    return False

def main():
    args = sys.argv
    
    try:
        if len(args) != 3 or not args[2].isdigit() or not check_string(args[1]):
            raise AssertionError()
        print(list(ft_filter(lambda x: len(x) > int(args[2]), args[1].split(" "))))
    except AssertionError:
        print("AssertionError: the arguments are bad")
    except Exception as e:
        print(f"something went wrong: {e}")

if __name__ == "__main__":
    main()