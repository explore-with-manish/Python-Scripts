# I want to log the arguments passed to the functions

# def add(a,b):
#     print("{} called with arguments {} {}".format("add", a,b))
#     return a+b

# def sub(a,b):
#     print("{} called with arguments {} {}".format("sub", a,b))
#     return a-b

# print(add(2,3))
# print(sub(2,3))

# ---------------------------------- HOF
# def hello():
#     print("Hello World")

# def hello_decorator(func):
#     def extendedLogic():
#         print("Some new implementation added")
#         func()
#     return extendedLogic

# # hello()

# hello = hello_decorator(hello)
# hello()

# -------------------------------

# def hello_decorator(func):
#     def extendedLogic():
#         print("Some new implementation added")
#         func()
#     return extendedLogic

# @hello_decorator
# def hello():
#     print("Hello World")

# hello()

# ----------------------------

def log(func):
    def logger(*args, **kwargs):
        print("{} called with arguments {}".format(func.__name__, args or kwargs))
        return func(*args, **kwargs)
    return logger

def exception_handler(func):
    def handler(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print("An error occurred in {}: {}".format(func.__name__, str(e)))
            return None
    return handler

@exception_handler
@log
def add(a,b):
    return a+b

@log("abc.txt")
def sub(a,b):
    return a-b

@exception_handler
def divide(a,b):
    return a/b

print(add(2,3))
print(add(2,'a'))
print(sub(2,3))
print(divide(2,0))