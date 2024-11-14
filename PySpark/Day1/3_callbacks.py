# If Function is considered as datatype, following should be applicable

# Can we create a variable of type int, inside a function
# If yes, we can also create a function, inside a function (Nested Function)

# Can we return a variable of type int, from a function
# If yes, we can also return a function, from a function (Closure, Fn Currying, HOF)

# Can we pass a variable of type int, to a function
# If yes, we can also pass a function, to a function (Callbacks)

# -------------------------------------- Internal API's using Callbacks
import functools
import operator

numList = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# # def processItem(item):
# #     return item*10

# # resultArr = []
# # for item in numList:
# #     resultArr.append(processItem(item))

# # resultArr = list(map(processItem, numList))

# resultArr = list(map(lambda item: item*10, numList))

# print(resultArr)

# sum = functools.reduce(lambda a, b: a+b, numList)
# print(sum)

# sum = functools.reduce(operator.add, numList)
# print(sum)

# evens = list(filter(lambda item: item%2==0, numList))
# print(evens)

# result = operator.mod(3, 2)
# print(result)

# ------------------------------------------

# def average(*numbers):
#     sum = 0
#     for n in numbers:
#         sum += n
#     if len(numbers):
#         return sum/len(numbers)
#     else:
#         return sum
    
# print(average(1,2))
# print(average(1,2,3,4,5))
# print(average(1,2,3,4,5,6,7,8,9))

# Dev 1
def average(callback, *numbers):
    sum = 0
    for n in numbers:
        sum += n
    if len(numbers):
        callback(sum/len(numbers))
    else:
        callback(sum)

# Dev 2
def processResult(result):
    print("Result is: ", result)

average(processResult, 1,2)
average(processResult, 1,2,3,4,5)
average(processResult, 1,2,3,4,5,6,7,8,9)