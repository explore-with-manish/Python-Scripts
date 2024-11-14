# print("List Iteration")
# l = ["Hello", "to", "everyone"]
# for i in l:
#     print(i)


# print("String Iteration")
# s = "Hello"
# for i in s:
#     print(i)


# print("Number Iteration")
# s = 1023010
# for i in s:             # TypeError: 'int' object is not iterable
#     print(i)


message = "Hello"
msgIterator = iter(message)
# print(dir(msgIterator))

# print(msgIterator.__next__())
print(next(msgIterator))
print(next(msgIterator))
print(next(msgIterator))
print(next(msgIterator))
print(next(msgIterator))
print(next(msgIterator))