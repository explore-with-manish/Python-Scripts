# non-default argument should not follow default argument
# def add(x=0, y=0):
#     return x+y

# print(add(2, 3))
# print(add(2))
# print(add())


# ------------------------------------------------  non-keyworded variable-length argument list
# Packing of Arguments
def average(*numbers):
    # print(type(numbers))
    # print(numbers)
    sum = 0
    for n in numbers:
        sum += n
    if len(numbers):
        return sum/len(numbers)
    else:
        return sum


# print(average())
# print(average(1))
# print(average(1, 2))
# print(average(1, 2, 3, 4, 5))
# print(average(1, 2, 3, 4, 5, 6, 7, 8, 9))

# numbersList = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# # numbersList = {1, 2, 3, 4, 5, 6, 7, 8, 9}
# # numbersList = (1, 2, 3, 4, 5, 6, 7, 8, 9)

# # Unpacking of Arguments
# # Spread a List (splat (*) operator)
# print(average(*numbersList))

# ----------------------------------------------------
# import copy
# # * on lefthand side of equalTo operator (Packing)
# # * on righthand side of equalTo operator (Unpacking)

# data1 = [[1, 2, 3, 4, 5], 20, 30, 40, 50]

# # data2 = data1

# # SHALLOW COPY
# # data2 = data1[::]
# # data2 = [*data1]
# # data2 = copy.copy(data1)

# # DEEP COPY
# data2 = copy.deepcopy(data1)

# print("data1: ", id(data1))
# print("data2: ", id(data2))
# print("data1: ", data1)
# print("data2: ", data2)

# data2[0][0] = 1000
# data2[1] = 2000

# print("\nAfter Modifying")
# print("data1: ", id(data1))
# print("data2: ", id(data2))
# print("data1: ", data1)
# print("data2: ", data2)


# ---------------------------------------------------- Destructuring

# data1 = [10, 20, 30, 40, 50]

# a = data1[0]
# b = data1[1]

# a, b = data1            # ValueError: too many values to unpack (expected 2)
# a, b, _, _, _ = data1
# a, _, _, _, b = data1

# a, b, *rest = data1
# a, *rest, b = data1

# print("a: ", a)
# print("b: ", b)
# print("rest: ", rest)

# a = 10
# b = 20

# print("Before-------")
# print("a: ", a)
# print("b: ", b)

# a, b = b, a

# print("\nAfter-------")
# print("a: ", a)
# print("b: ", b)

# ------------------------------------------------------ keyworded, variable-length argument list
# def printData(id, name="Abhijeet", city="Pune"):
#     print("Id: ", id)
#     print("Name: ", name)
#     print("City: ", city)

# printData(1)
# printData(1, "Manish", "Mumbai")
# printData(1, "Mumbai")

# printData(id=10, name="Manish", city="Mumbai")
# printData(name="Manish", city="Mumbai", id=10)
# printData(id=10, city="Mumbai")

def printData(**kwargs):
    print(kwargs)
    print(type(kwargs))

# printData(1, "Manish", "Mumbai")  # TypeError: printData() takes 0 positional arguments but 3 were given
# printData(id=10, name="Manish", city="Mumbai")


myEmployee = {"id": 10, "name": "Manish", "city": "Mumbai"}
# printData(myEmployee)       # TypeError: printData() takes 0 positional arguments but 1 was given
printData(**myEmployee)