# def hello():
#     pass

# def hello():
#     print('Hello World')

# hello()
# print(hello)
# print(type(hello))


# def add(x, y):
#     return x+y


# print(add(2, 3))
# print(add(2, 3, 4))             # add() takes 2 positional arguments but 3 were given
# print(add(2))                     # add() missing 1 required positional argument: 'y'

# def addAll(numbers):
#     print(numbers)
#     print(type(numbers))


# addAll([2, 3, 4, 5])
# addAll(2)
# addAll(["2", "3"])
# addAll("Manish")
# addAll({"name": "Manish"})
# addAll(("2", "3"))


def hello(name: str) -> str:
    print(type(name))
    # return (f"Hello {name}")
    return 100


print(hello("Manish"))
print(hello(10))
