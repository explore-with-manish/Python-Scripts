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

# # class Manager(Employee):
# #     pass

# class Manager(Employee):
#     def __init__(self, id=0, name="NA", desig="NA", sal=0, location="Pune"):
#         super().__init__(id, name, desig, sal)
#         self._location = location
    
#     def getLocation(self):
#         return self._location
    
#     def setSalary(self, value):
#         if(value < 100000):
#             raise ValueError("I will not work less than 100000")
#         self._salary = value

# e = Manager(1, "Manish", "Trainer", 12345, "Mumbai")
# print("Id: ", e.getId())
# print("Name: ", e.getName())
# print("Designation: ", e.getDesignation())
# print("Salary: ", e.getSalary())
# print("Location: ", e.getLocation())

# try:
#     e.setSalary(11000)
#     print("Salary: ", e.getSalary())
# except Exception as exp:
#     print(exp)

# # print(Manager.mro())

# ----------------------------------------------------- Multiple Inheritance

# class A:
#     def __init__(self):
#         print("Class A init")

#     def methodA(self):
#         print("Class A Method")
    
#     def methodS(self):
#         print("Class A Method S")

# class B:
#     def __init__(self):
#         print("Class B init")

#     def methodB(self):
#         print("Class B Method")

#     def methodS(self):
#         print("Class B Method S")

# class C(B, A):
#     def __init__(self):
#         super().__init__()
#         print("Class C init")

# obj = C()
# obj.methodA()
# obj.methodB()
# obj.methodS()

# print(C.mro())

class A:
    def __init__(self):
        print("Class A init")

    def methodA(self):
        print("Class A Method")
    
    def methodS(self):
        print("Class A Method S")

class B(A):
    def __init__(self):
        super().__init__()
        print("Class B init")

    def methodB(self):
        print("Class B Method")

    def methodS(self):
        super().methodS()
        print("Class B Method S")

class C(B):
    def __init__(self):
        super().__init__()
        print("Class C init")

obj = C()
obj.methodA()
obj.methodB()
obj.methodS()

# print(C.mro())