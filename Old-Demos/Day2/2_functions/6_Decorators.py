# Decorators can add functionality to an existing code

# This is also called metaprogramming because a part of the program
# tries to modify another part of the program at compile time


# def hello():
#     print("Hello World")

# # hello()


# def hello_decorator(func):
#     def extendedLogic():
#         print("Some new implemenetation added")
#         func()
#     return extendedLogic


# # extended_logic = hello_decorator(hello)
# # extended_logic()

# hello = hello_decorator(hello)
# hello()

# -------------------------------------------------

# def hello_decorator(func):
#     def extendedLogic():
#         print("Some new implemenetation added")
#         func()
#     return extendedLogic


# @hello_decorator
# def hello():
#     print("Hello World")

# hello()

# ----------------------------------------------------
# Create a decorator to log the following when function is called
# print("{} called with arguments {}".format(func.__name__, (a, b)))

def log(func):
    def logger(*args, **kwargs):
        print("{} called with arguments {}".format(func.__name__, args or kwargs))
        return func(*args, **kwargs)
    return logger

@log
def add(a, b):
    return a+b

@log
def sub(a, b, c):
    return a-b-c


print(add(2, 3))
print(add(a=20, b=30))
print(sub(20, 10, 5))
print(sub(a=20, b=10, c=5))
