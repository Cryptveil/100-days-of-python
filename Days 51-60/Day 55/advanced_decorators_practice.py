def logging_decorator(function):
    def wrapper_function(*args):
        print(f"You called {function.__name__}{args}")
        result = function(args[0], args[1], args[2])
        print(f"It returned: {result}")
    return wrapper_function


@logging_decorator
def add(a, b, c):
    return a * b * c


add(1, 2, 3)
