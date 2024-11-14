# ---------------------------------------- DefaultDict
from collections import defaultdict

numbers = defaultdict(int)
# numbers = dict()

numbers["one"] = 1
numbers["two"] = 2
numbers["three"] = 3
numbers["four"] = "four"

# print(numbers)
# print(type(numbers))

for i in numbers.items():
    print(i)

# ---------------------------------------- Tuple
# Employee = ("Manish", "Sharma", "Pune")
# print(type(Employee))

# for attribute in Employee:
#     print(attribute)

# print(Employee[0])
# print(Employee[1])
# print(Employee[2])

# ---------------------------------------- Named Tuple
# from collections import namedtuple

# Employee = namedtuple('Employee', 'fname, lname, city')

# # e1 = Employee("Manish", "Sharma", "Pune")
# # print(e1)

# # print(e1[0])
# # print(e1[1])
# # print(e1[2])

# # print(e1.fname)
# # print(e1.lname)
# # print(e1.city)

# empList = [Employee("Pravin", "Dabade", "Pune"), Employee(
#     "Manish", "Sharma", "Pune"), Employee("Abhijeet", "Gole", "Pune")]

# for e in empList:
#     print(e.fname)
#     print(e.lname)
#     print(e.city)
#     print()

# ---------------------------------------- Counter
# from collections import Counter

# list = [1, 2, 3, 4, 1, 2, 6, 7, 3, 8, 1, 2, 2]
# r = Counter(list)
# print(r)
