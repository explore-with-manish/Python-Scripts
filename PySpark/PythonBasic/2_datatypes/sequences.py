# ------------------------------- list
# # data = list()
# data = [1, 2, 3, 4, 5, "Pune"]

# # print(data)
# # print(type(data))

# # print(data[0])
# # print(data[1:4])

# print(data)
# print(id(data))

# # data.append(6)
# # print(data)
# # print(id(data))

# # data[0] = "Changed"
# data = [1, 2]
# print(data)
# print(id(data))

# --------------------------------------------------- Tuple

# # data = tuple()
# data = (1, 2, 3, 4, 5, "Pune")
# # print(data)
# # print(type(data))

# # print(data[0])
# # print(data[1:4])

# print(data)
# print(id(data))

# # data.append(6)
# # data[0] = "Changed"
# data = (1, 2)
# print(data)
# print(id(data))

# # --------------------------------------------------- Set
# # data = set()
# data = {1, 2, 3, 4, 5, "Pune", 6, 2, 9, 4, 5, "Mumbai"}
# print(data)
# print(type(data))

# ----------------------------------------------------- Dictionary

# data = dict()

# data = {"Manish": 9999999999, "Abhijeet": 8888888888, "Ramakant": 7777777777}
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

# n_range = range(0, 10)
# print(n_range)
# print(type(n_range))

# # for a in n_range:
# #     print(a)

# # data = list(n_range)
# # data = tuple(n_range)
# data = set(n_range)


# print(data)
# print(type(data))


# -----------------------------------------------

data = [2, 4, 3, 1, 1, 4]

r = set(data)
print(r)

# ------------------------------
# Write a logic to get the below given output
# Result - {2: 1, 4: 2, 3: 1, 1: 2}

# r = {}

# for i in data:
#     if i in r:
#         r[i] = r[i] + 1
#     else:
#         r[i] = 1

# print(r)

# -------------
# r = {}

# for i in set(data):
#     r[i] = data.count(i)

# print(r)

# -------------------------------------
# r = dict((i, data.count(i)) for i in set(data))
# print(r)

# -------------------------------------
# from collections import Counter

# r = dict(Counter(data))
# print(r)
# print(sorted(r.items()))
