# class MyRange:
#     def __init__(self, limit):
#         self._limit = limit

#     def __iter__(self):
#         self._x = 1
#         return self

#     def __next__(self):
#         x = self._x

#         if(x > self._limit):
#             raise StopIteration

#         self._x = x+1
#         return x

# # for i in range(5):
# #     print(i)


# # for i in MyRange(5):
# #     print(i)

# print(list(range(20)))
# print(list(range(1, 21)))
# print(list(MyRange(20)))

# ----------------------------------------------------------------

# class Queue:
#     def __init__(self):
#         self._children = []

#     def push(self, data):
#         self._children.append(data)

#     def __iter__(self):
#         return iter(self._children)
        
#     # def __iter__(self):
#     #     for i in self._children:
#     #         yield i

class Queue:
    def __init__(self):
        self._children = []

    def push(self, data):
        self._children.append(data)

    def __iter__(self):
        self._index = 0  # Reset index for iteration
        return self

    def __next__(self):
        if self._index >= len(self._children):
            raise StopIteration  # Stop iteration when all elements are exhausted
        result = self._children[self._index]
        self._index += 1  # Move to the next index
        return result


numbersQ = Queue()

numbersQ.push(10)
numbersQ.push(20)
numbersQ.push(30)

for n in numbersQ:
    print(n)
