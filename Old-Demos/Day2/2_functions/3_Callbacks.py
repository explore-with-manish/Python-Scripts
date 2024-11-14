# If Function is considered as datatype, following should be applicable

# Can we create a variable of type int, inside a function
# If yes, we can also create a variable of type function, inside a function

# Can we return a variable of type int, from a function
# If yes, we can also return a variable of type function, from a function

# Can we pass a variable of type int, to a function
# If yes, we can also pass a variable of type function, to a function

# def average(*numbers):
#     sum = 0
#     for n in numbers:
#         sum += n
#     if len(numbers):
#         return sum / len(numbers)
#     else:
#         return sum


# result = average(1, 2, 3, 4, 5, 6, 7, 8, 9)
# print(result)

# ---------------------------------------------- Fn Passed as argument to another Fn

# Dev 1
# def average(callback, *numbers):
#     sum = 0
#     for n in numbers:
#         sum += n
#     if len(numbers):
#         callback(sum / len(numbers))
#     else:
#         callback(sum)


# # Dev 2
# # def printResult(result):
# #     print("Result is: ", result)


# # average(printResult, 1, 2)
# # average(printResult, 1, 2, 3, 4, 5)
# # average(printResult, 1, 2, 3, 4, 5, 6, 7, 8, 9)

# average(lambda result: print("Result is: ", result), 1, 2, 3, 4, 5, 6, 7, 8, 9)

# -----------------------------------------------------------------

# numList = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# def processItem(item):
#     return item*10

# resultArr = []
# for item in numList:
#     resultArr.append(processItem(item))

# print(resultArr)

# resultArr = list(map(processItem, numList))
# print(resultArr)

# resultArr1 = list(map(lambda item: item*10, numList))
# print(resultArr1)

# resultArr2 = list(map(lambda item: item*5, numList))
# print(resultArr2)

# def fn(item):
#     x = item+1
#     return x*100

# resultArr3 = list(map(lambda item: fn(item), numList))
# print(resultArr3)

# -----------------------------------------------------------------
# import functools
# import operator

# numList = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# # sum = functools.reduce(lambda a, b: a+b, numList)
# # print("Sum: ", sum)

# # r = functools.reduce(lambda a, b: a if a > b else b, numList)
# # print("Max: ", r)

# # sum = functools.reduce(operator.add, numList)
# # print("Sum: ", sum)

# # pr = functools.reduce(operator.mul, numList)
# # print("Product: ", pr)

# r = functools.reduce(max, numList)
# print("Max: ", r)


# ------------------------------------------------------------------
numList = [1, 2, 3, 4, 5, 6, 7, 8, 9]

evens = list(filter(lambda item: item % 2 == 0, numList))
print(evens)
