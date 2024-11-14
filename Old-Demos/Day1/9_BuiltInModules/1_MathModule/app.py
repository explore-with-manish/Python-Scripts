# import math
# # print(math)

# result = math.sqrt(81)
# print(result)

# print(math.factorial(5))
# print(math.factorial(6))

# n = 5
# k = 3

# r = math.factorial(n) / (math.factorial(k)*math.factorial(n-k))
# print(r)

# --------------------------------------------------------------------------------

# from math import factorial, sqrt

# result = sqrt(81)
# print(result)

# print(factorial(5))
# print(factorial(6))

# n = 5
# k = 3

# r = factorial(n) / (factorial(k)*factorial(n-k))
# print(r)

# --------------------------------------------------------------------------------

# from math import factorial as f, sqrt as s

# result = s(81)
# print(result)

# print(f(5))
# print(f(6))

# n = 5
# k = 3

# r = f(n) / (f(k)*f(n-k))
# print(r)

# How many ways can first and second place be awarded to 10 people?

from math import factorial
from itertools import permutations
l = list(range(1, 11))
# print(l)

# print(list(permutations(l, 2)))
print(len(list(permutations(l, 2))))

n = 10
r = 2

p = factorial(n) / factorial(n-r)
print(p)
