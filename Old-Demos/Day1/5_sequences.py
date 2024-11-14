# ---------------------------------------- List
# data = list()
# data = [1, 2, 3, 4, 5, "Pune"]
# print(data)
# print(type(data))

# print(data[0])
# print(data[1:4])

# print(data)
# print(id(data))
# # data.append(6)
# # data[0] = "Changed"
# # data = [1, 2]
# print(data)
# print(id(data))

# --------------------------------------------------- Tuple
# data = tuple()
# data = (1, 2, 3, 4, 5, "Pune")

# # print(data)
# # print(type(data))

# # print(data[0])
# # print(data[1:4])

# print(data)
# print(id(data))
# # data.append(6)          # AttributeError: 'tuple' object has no attribute 'append'
# # data[0] = "Changed"     # TypeError: 'tuple' object does not support item assignment
# data = (1, 2)
# print(data)
# print(id(data))

# --------------------------------------------------------- Set
# data = set()
# data = {1, 2, 3, 4, 5, "Pune", 1, 2, 3, 4, 5, "Pune"}
# print(data)
# print(type(data))

# for a in data:
#     print(a)

# --------------------------------------------------------- Dictionary (Dict)

# data = dict()
# data = {
#     "Manish": 9999999999,
#     "Abhijeet": 8888888888,
#     "Ramakant": 7777777777
# }
# print(data)
# print(type(data))

# for a in data:
#     print(a)
# for a in data.keys():
#     print(a)

# for a in data.items():
#     print(a)

# for a in data.values():
#     print(a)

# --------------------------------------------------------- Range
# nRange = range(0, 10)
# print(nRange)
# print(type(nRange))

# for a in nRange:
#     print(a)

# data = list(nRange)
# data = tuple(nRange)
# data = set(nRange)

# print(data)
# print(type(data))

# for a in nRange:
#     print(a)
#     print("Inside Loop")

# print("Outside Loop")

# ----------------------------------------------- Input and create a dynamic list
numberList = []

n = int(input("Enter number of items: "))

for i in range(n):
    inp = int(input("Enter a number: "))
    numberList.append(inp)

print(numberList)
print(numberList + [45, 60])
print(numberList * 3)

print(10 in numberList)
print(10 not in numberList)

print(numberList[1])
print(numberList[1:5])