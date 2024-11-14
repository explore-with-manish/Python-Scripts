from collections import Counter, OrderedDict
data = [2, 4, 3, 1, 1, 4]

# r = set(data)
# print(r)

# ------------------------------
# Write a logic to get the below given output
# Result - {2: 1, 4: 2, 3: 1, 1: 2}

# r = {}

# for i in data:
#     if i in r:
#         r[i] = r[i]+1
#     else:
#         r[i] = 1

# print(r)

# --------------------------------------------------
# print(data.count(1))
# r = {}

# for i in set(data):
#     r[i] = data.count(i)

# print(r)

# ------------------------------------------------- Comprehension
# r = dict((i, data.count(i)) for i in set(data))
# print(r)

# -------------------------------------------------- Counter from collections Module
r = dict(Counter(data))
print(r)
print(sorted(r.items()))
