# class Employee:
#     def __init__(self, id=0, name="NA", desig="NA", sal=0):
#         self._id = id
#         self._name = name
#         self._designation = desig
#         self._salary = sal

#     def getId(self):
#         return self._id

#     def getName(self):
#         return self._name

#     def getDesignation(self):
#         return self._designation

#     def getSalary(self):
#         return self._salary

#     def setSalary(self, value):
#         if(value < 10000):
#             raise ValueError("I will not work less than 10000")
#         self._salary = value

#     Salary = property(getSalary, setSalary)


# e = Employee(1, "Manish", "Trainer", 12345)
# print("Id: ", e.getId())
# print("Name: ", e.getName())
# print("Designation: ", e.getDesignation())
# print("Salary: ", e.Salary)

# try:
#     e.Salary = 0
#     print("Salary: ", e.Salary)
# except Exception as exp:
#     print(exp)

# ------------------------------------------------------------------- Using Decorator
# class Employee:
#     def __init__(self, id=0, name="NA", desig="NA", sal=0):
#         self._id = id
#         self._name = name
#         self._designation = desig
#         self._salary = sal

#     def getId(self):
#         return self._id

#     def getName(self):
#         return self._name

#     def getDesignation(self):
#         return self._designation

#     @property
#     def Salary(self):
#         return self._salary

#     @Salary.setter
#     def Salary(self, value):
#         if(value < 10000):
#             raise ValueError("I will not work less than 10000")
#         self._salary = value


# e = Employee(1, "Manish", "Trainer", 12345)
# print("Id: ", e.getId())
# print("Name: ", e.getName())
# print("Designation: ", e.getDesignation())
# print("Salary: ", e.Salary)

# try:
#     e.Salary = 0
#     print("Salary: ", e.Salary)
# except Exception as exp:
#     print(exp)

# --------------------------------------------------------------------------------

class Employee:
    def __init__(self, id=0, name="NA", desig="NA", sal=0):
        self._id = id
        self._name = name
        self._designation = desig
        self._salary = sal

    @property
    def Id(self):
        return self._id

    @property
    def Name(self):
        return self._name

    @property
    def Designation(self):
        return self._designation

    @property
    def Salary(self):
        return self._salary

    @Salary.setter
    def Salary(self, value):
        if(value < 10000):
            raise ValueError("I will not work less than 10000")
        self._salary = value


e = Employee(1, "Manish", "Trainer", 12345)
print("Id: ", e.Id)
print("Name: ", e.Name)
print("Designation: ", e.Designation)
print("Salary: ", e.Salary)

try:
    e.Salary = 0
    print("Salary: ", e.Salary)
except Exception as exp:
    print(exp)
