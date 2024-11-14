# def sqrt(x):
#     guess = x
#     i = 0
#     while guess * guess != x and i < 20:
#         guess = (guess + x/guess)/2.0
#         i += 1
#     return guess

# print(sqrt(9))
# print(sqrt(2))
# print(sqrt(-1))

# -----------------------------------------------------------------

# def sqrt(x):
# if(x < 0):
#     raise ValueError("Error: Cannot use negative number {}".format(x))
#     guess = x
#     i = 0
#     while guess * guess != x and i < 20:
#         guess = (guess + x/guess)/2.0
#         i += 1
#     return guess

# def sqrt(x):
#     guess = x
#     i = 0
#     try:
#         while guess * guess != x and i < 20:
#             guess = (guess + x/guess)/2.0
#             i += 1
#     except ZeroDivisionError:
#         # Log the actual Exception
#         raise ValueError("Error: Cannot use negative number {}".format(x))
#     return guess

def sqrt(x):
    if(x < 0):
        raise ValueError("Error: Cannot use negative number {}".format(x))
    guess = x
    i = 0
    try:
        while guess * guess != x and i < 20:
            guess = (guess + x/guess)/2.0
            i += 1
    except Exception:
        # Log the actual Exception
        raise Exception("Error: Executing Logic")
    return guess


try:
    print(sqrt(9))
    print(sqrt(2))
    print(sqrt(-1))
except Exception as e:
    print(e)
