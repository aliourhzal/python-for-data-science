import sys

def even_odd():
    args = sys.argv
    num_args = len(args)

    try:
        if num_args < 2:
            return 
        if num_args > 2:
            raise AssertionError("more than one argument is provided")
        if not args[1].lstrip('+-').isdigit():
            raise AssertionError(" argument is not an integer")
        
        num = int(args[1])
        print("I'm Even.") if num % 2 == 0 else print("I'm Odd.")
    except Exception as e:
        print(f"AssertionError: {e}")
    

even_odd()