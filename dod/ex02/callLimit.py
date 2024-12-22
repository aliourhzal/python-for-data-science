def callLimit(limit: int):
    count = 0
    def callLimiter(function):
        def limit_function(*args: any, **kwds: any):
            nonlocal count

            if count < limit:
                function(*args, **kwds)
                count += 1
            else:
                print(f"Error: {function} call too many times")
        return limit_function
    return callLimiter


# @callLimit(3)
# def f():
#     print ("f()")

# @callLimit(1)
# def g():
#     print ("g()")

# for i in range(3):
#     f()
#     g()

def decorator_wrapper(count):
    def hello_decorator(func):
        nonlocal count
        count += 1
        print(f"decorator used {count} times")
        def exec_func(*args, **kwds):
            print("before")
            func(*args, **kwds)
            print("after")
        return exec_func
    return hello_decorator

decorator = decorator_wrapper(0)

@decorator
def test():
    print("this is test function")

test()

@decorator
def hello():
    print("hello world")

hello()



