# from itertools import permutations, combinations

# data = 'ABCD'

# result1 = permutations(data, 2)
# print(list(result1))

# result2 = combinations(data, 2)
# print(list(result2))

# ----------------------------------------------------------
from itertools import groupby

colors = ["blue", "red", "blue", "yellow", "blue", "red"]

# r = [(i, len(list(c))) for i, c in groupby(colors)]
# r = [(i, len(list(c))) for i, c in groupby(sorted(colors))]
# r = [(i, len(list(c))) for i, c in groupby(sorted(colors, reverse=True))]

print(r)

# ----------------------------------------------------------
# from itertools import accumulate
# data = [1, 2, 3, 4, 5]

# result = accumulate(data)
# print(list(result))

# ---------------------------------------------------------
# from itertools import accumulate
# from operator import mul
# data = [1, 2, 3, 4, 5]

# result = accumulate(data, mul)
# print(list(result))

# ---------------------------------------------------------
# from itertools import accumulate

# data = [5, 2, 6, 4, 5, 9, 1]

# result = accumulate(data, max)
# print(list(result))

# ---------------------------------------------------------
import time
import operator

data1 = [1, 2, 3, 4] * 10000
data2 = [5, 6, 7, 8] * 10000

t1 = time.time()

result2 = list(map(operator.mul, data1, data2))

t2 = time.time()
# print("Result:", result2)
print(f"\nTime taken by map function: {t2 - t1}")

# -----------------------------------------------------

t1 = time.time()

result1 = []
for i, value in enumerate(data1):
    result1.append(data1[i] * data2[i])

t2 = time.time()
# print("Result:", result1)
print(f"\nTime taken by map function: {t2 - t1}")


# def fn(n):
#     return n*10

# data1 = [1, 2, 3, 4]

# result = map(fn, data1)
# print(list(result))


# def fn(n):
#     return n.upper()

# data1 = ["manish","ramakant","abhijeet","pravin"]

# result = map(fn, data1)
# print(list(result))
