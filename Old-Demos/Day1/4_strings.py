"""This module demonstrates variable declarations, printing, type checking, slicing,
and concatenation in Python using basic string and integer operations.
"""

name1 = "Synechron"
name2 = "Pune Phase 3"
name3 = "A"

print(name1)
print(type(name1))

print(name2)
print(type(name2))

print(name3)
print(type(name3))

name4 = """Hi There
    Hello
    How Are You
            Test"""
print(name4)
print(type(name4))

name5 = """Hi There
    Hello
    How Are You
            Test"""
print(name5)
print(type(name5))

a = '"Hello"'
print(a)
# print(type(a))

print(a[0])
print(a[1])
print(a[1:9])
# print(a[9])

t = a[1:9]
print(t)
print(len(t))
print(t + "check")

print(type(a[1]))

n = 10
print(n)
print(type(n))

message = "Number is "
print(message + str(n))

# for c in message:
#     print(c)
