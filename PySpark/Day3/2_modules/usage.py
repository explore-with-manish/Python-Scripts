# import words
# result = words.fetch_words()
# print(result)

# from words import fetch_words
# result = fetch_words()
# print(result)

# ---------------------------------
# import check.words
# import words

# result = words.fetch_words()
# print(result)

# result1 = check.words.fetch_words()
# print(result1)

# # --------------------------------- Alias

# from words import fetch_words as fw1
# result = fw1()
# print(result)

# from check.words import fetch_words as fw2
# result = fw2()
# print(result)

# -------------------------------------
# from my_utils.module1 import greet
# from my_utils.module2 import add

from my_utils import greet, add, Employee

print(greet("Manish"))  # Output: Hello, Manish!
print(add(5, 7))        # Output: 12

e = Employee(1, "Manish", "Trainer", 12345)
print("Id: ", e.getId())
print("Name: ", e.getName())
print("Designation: ", e.getDesignation())
print("Salary: ", e.Salary)
