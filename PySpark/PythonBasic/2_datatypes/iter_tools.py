# from itertools import permutations, combinations

# data = "ABCD"
# result_one = permutations(data, 2)
# print(list(result_one))

# result_two = combinations(data, 2)
# print(list(result_two))

# --------------------------------
# from itertools import groupby

# colors = ["blue", "red", "blue", "yellow", "blue", "red"]

# # r = [(i, len(list(c))) for i, c in groupby(colors)]
# # r = [(i, len(list(c))) for i, c in groupby(sorted(colors))]
# r = [(i, len(list(c))) for i, c in groupby(sorted(colors, reverse=True))]

# print(r)

# ---------------------------------------
import time
import operator

data1 = [1, 2, 3, 4]
data2 = [5, 6, 7, 8]

t1 = time.time()

# result1 = []
# for i in range(len(data1)):
#     result1.append(data1[i] * data2[i])

result2 = list(map(operator.mul, data1, data2))

t2 = time.time()

# print("Result:", result1)
print("Result:", result2)
print("\nTime taken by for loop: %.16f" % (t2 - t1))
