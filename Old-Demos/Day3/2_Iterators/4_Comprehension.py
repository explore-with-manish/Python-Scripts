words = """Lorem ipsum dolor sit amet consectetur adipisicing elit.
Reiciendis eum, laudantium harum voluptas, debitis aliquid porro accusantium ducimus corporis
sit aspernatur tenetur magnam vitae nesciunt officiis aperiam cupiditate similique explicabo.""".split()

print(words)
print(type(words))

# Write a logic to, create a List of numbers representing length of each word in words list
wlength = []
for word in words:
    wlength.append(len(word))

print(wlength)

# wlenght = list(map(lambda word: len(word), words))
# print(wlenght)

# ----------------------------------------------------- Comprehension

# List Comprehension - [exp(item) from item in iterable if exp]
# Dict Comprehension - {exp(item) from item in iterable if exp}

# wlength = [len(word) for word in words]
# print(wlength)

# from math import factorial

# factorials = [factorial(n) for n in range(0, 21)]
# print(factorials)

# factorials_len = [len(str(factorial(n))) for n in range(0, 21)]
# print(factorials_len)

# inpList = list(range(0, 21))
# n = "abc"
# print("Before, ", n)

# # evList = []
# # for n in inpList:
# #     if n % 2 == 0:
# #         evList.append(n)

# evList = [n for n in inpList if n % 2 == 0]

# print(evList)
# print("After, ", n)

# ---------------------------------- Square of each number from range 0, 21

# result = [x*x for x in range(0, 21)]
# result = {x*x for x in range(0, 21)}
# result = {x: x*x for x in range(0, 21)}

# print(result)
# print(type(result))


# ------------------------------------------------------------

# data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# flatData = []
# for item in data:
#     for value in item:
#         flatData.append(value)

# flatData = [value for item in data for value in item]
# print(flatData)

# Generator Comprehension
# flatData = (value for item in data for value in item)
# print(flatData)
# print(list(flatData))


# ----------------------------------------------------------

countrycapital = {
    "India": "Delhi",
    "Morocco": "Rabat",
    "Netherlands": "Amsterdam",
    "UAE": "Abu Dhabi",
}


capitalcountry = {capital: country for country, capital in countrycapital.items()}

print(countrycapital)
print(capitalcountry)
