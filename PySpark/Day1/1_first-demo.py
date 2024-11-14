# def hello():
#     pass

# print(hello)
# print(type(hello))

# def add(x,y):
#     return x+y

# def add(x,y=0):
#     return x+y

# print(add(2,3))
# # print(add(2,3,4))   
# print(add(2))   

def average(*numbers):
    print(numbers)

average()
average(1)
average(1,2)
average(1,2,3,4,5)
average(1,2,3,4,5,6,7,8,9)

# def printData(**kwargs):
#     print(kwargs)

# # printData(1,"Manish")
# # printData(id=1,name="Manish")

# e1={"id":1, "name":"Manish"}
# # printData(e1)
# printData(**e1)
