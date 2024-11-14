# def idGenerator():
#     yield 1
#     yield 2
#     yield 3

# # print(dir(idGenerator()))

# # for i in idGenerator():
# #     print(i)

# genObj = idGenerator()
# print(next(genObj))
# print(next(genObj))
# print(next(genObj))
# print(next(genObj))

class Queue:
    def __init__(self):
        self._children = []

    def push(self, data):
        self._children.append(data)
    
    def __iter__(self):
        for i in self._children:
            yield i

numbersQ = Queue()

numbersQ.push(10)
numbersQ.push(20)
numbersQ.push(30)

for n in numbersQ:
    print(n)