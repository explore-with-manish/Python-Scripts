# r, w, a
# r+, w+, a+
# rb, wb, ab
# rb+, wb+, ab+

# fo = open("file1.txt", "w+")
# print("Name of the file ", fo.name)
# print("Mode of the file ", fo.mode)
# fo.close()
# print("Closed Status, of the file ", fo.closed)

# input = "This is just an example of File Write.\nUsing Python"

# fo = open("file1.txt", "w+")
# fo.write(input)

# fo = open("file1.txt", "wb+")
# binp = bytearray(input, "utf-8")
# fo.write(binp)

# fo = open("file1.txt", "w+")
# fo.write(input)

# position = fo.tell()
# print("Current Cursor position", position)

# position = fo.seek(0)
# print("Current Cursor position", position)

# str = fo.read()
# str = fo.read(10)
# str = fo.readline()
# str = fo.readlines()
# print(str)

# while True:
#     s = fo.readline()
#     if not s:
#         break
#     print(s)

# for line in fo.readlines():
#     print(line)
#     print(type(line))

# ---------------------------------------------------------
import json
from pprint import pprint as pp

# employee = {
#     "name": "Manish",
#     "age": 38,
#     "city": "Pune"
# }

# print(employee)
# print(type(employee))

# y = json.dumps(employee)
# print(y)
# print(type(y))

# fo = open('data.json', "w")
# json.dump(employee, fo)
# fo.close()

# fo = open('data.json', "r")
# data = json.load(fo)

# print(data)
# print(type(data))

# fo = open('user.json', "r")
# data = json.load(fo)

# print(data)
# print(type(data))

fo = open('posts.json', "r")
data = json.load(fo)

pp(data)