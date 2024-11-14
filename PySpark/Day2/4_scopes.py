# L - Local
# E - Enclosing
# G - Global
# B - Built In

# --------------------------

# def len(inp):
#     print("my len fn called...")
#     return 0

# print(len("Hello"))

# ---------------------------

x = 10

# def show():
#     print("Inside Show, x:", x)

# def show():
#     x = 1000
#     print("Inside Show, x:", x)

# def show():
#     global x
#     x = 1000
#     print("Inside Show, x:", x)

# show()
# print("Outside Show, x:", x)

# ----------------------------

x = 10

# def show():
#     def check():
#         print("Inside Check, x:", x)

#     check()
#     print("Inside Show, x:", x)

# def show():
#     x = 100
#     def check():
#         # global x
#         nonlocal x
#         x = 1000
#         print("Inside Check, x:", x)

#     check()
#     print("Inside Show, x:", x)

# show()
# print("Outside Show, x:", x)

# ------------------------------- Block Scoping not supported
i = "Hello"
print("Before, i: ", i)

# for i in range(5):
#     print("Inside Loop, i is: ", i)

def iterate():
    for i in range(5):
        print("Inside Loop, i is: ", i)

iterate()

print("After, i: ", i)

# -------------------------

# function (include lambda)
# module
# class
# generator expression
# comprehensions

