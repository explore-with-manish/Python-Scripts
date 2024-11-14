# class Employee:
#     pass


# class Employee:
#     def __init__(self, id):
#         self._id = id

#     # def __repr__(self):
#     #     return f"Employee Id is {self._id}"

#     def __str__(self):
#         return f"String Employee Id is {self._id}"


# a = int(10)
# print(a)
# print(type(a))
# print(str(a))

# e = Employee(1)
# print(e)
# print(type(e))
# print(str(e))

# class Employee:
#     def __init__(self, id):
#         self._id = id


# e1 = Employee(1)
# print(e1._id)

# e2 = Employee(2)
# print(e2._id)

# print(e1 > e2)
from functools import total_ordering


@total_ordering
class Employee:
    def __init__(self, id=0, name="NA", desig="NA", sal=0):
        self._id = id
        self._name = name
        self._designation = desig
        self._salary = sal

    def getId(self):
        return self._id

    def getName(self):
        return self._name

    def getDesignation(self):
        return self._designation

    def getSalary(self):
        return self._salary

    def setSalary(self, value):
        if(value < 10000):
            raise ValueError("I will not work less than 10000")
        self._salary = value

    def __gt__(self, obj):
        return self._salary > obj._salary

    def __eq__(self, obj):
        return self._salary == obj._salary

    def __add__(self, obj):
        return self._salary + obj._salary


# e = Employee()
e = Employee(1, "Manish", "Trainer", 12345)
print("Id: ", e.getId())
print("Name: ", e.getName())
print("Designation: ", e.getDesignation())
print("Salary: ", e.getSalary())

try:
    e.setSalary(0)
    print("Salary: ", e.getSalary())
except Exception as exp:
    print(exp)


e1 = Employee(2, "Abhijeet", "Trainer", 12345)
print("Id: ", e1.getId())
print("Name: ", e1.getName())
print("Designation: ", e1.getDesignation())
print("Salary: ", e1.getSalary())

print(e1 > e)
print(e1 < e)
print(e1 == e)

print(e1 + e)
