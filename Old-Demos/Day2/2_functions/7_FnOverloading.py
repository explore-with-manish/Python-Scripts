# def add(a, b):
#     return a+b


# def add(a, b, c):
#     return a+b+c


# print(add(2, 3))
# print(add(2, 3, 4))

# -----------------------------------------------------
# def getAdd():
#     def m1(a, b):
#         return a+b

#     def m2(a, b, c):
#         return a+b+c

#     def add(*args):
#         if(len(args) == 2):
#             return m1(*args)
#         elif(len(args) == 3):
#             return m2(*args)
#         else:
#             raise Exception("No Implemenattion Found")

#     return add


# add = getAdd()

# print(add(2, 3))
# print(add(2, 3, 4))

# try:
#     print(add(2))
# except Exception as e:
#     print(e)

# -----------------------------------------------------
def add(*args):
    if(len(args) == 2):
        return args[0] + args[1]
    elif(len(args) == 3):
        return args[0] + args[1] + args[2]
    else:
        raise Exception("No Implemenattion Found")

print(add(2, 3))
print(add(2, 3, 4))

try:
    print(add(2))
except Exception as e:
    print(e)
