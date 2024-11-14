# l = ["Hello", "to", "everyone"]
# for i in l:
#     print(i)

# l = "Hello"
# for i in l:
#     print(i)

# l = 123456      #TypeError: 'int' object is not iterable
# for i in l:
#     print(i)

message = "Hello"
msgIterator = iter(message)
# print(dir(msgIterator))

# print(msgIterator.__next__())
# print(msgIterator.__next__())
# print(msgIterator.__next__())
# print(msgIterator.__next__())
# print(msgIterator.__next__())
# print(msgIterator.__next__())

print(next(msgIterator))
print(next(msgIterator))
print(next(msgIterator))
print(next(msgIterator))
print(next(msgIterator))
print(next(msgIterator))
