class Queue:
    def __init__(self):
        self._children = []

    def push(self, data):
        self._children.append(data)
    
    def __iter__(self):
        self._index = 0
        return self

    def __next__(self):
        if self._index >= len(self._children):
            raise StopIteration
        result = self._children[self._index]
        self._index+=1
        return result

numbersQ = Queue()

numbersQ.push(10)
numbersQ.push(20)
numbersQ.push(30)

for n in numbersQ:
    print(n)