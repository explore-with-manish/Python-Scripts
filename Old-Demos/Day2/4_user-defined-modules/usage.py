# import words
# result = words.fetch_words()
# print(result)

# from words import fetch_words
# result = fetch_words()
# print(result)

# ---------------------------------------------------
# import check.words
# import words

# result1 = check.words.fetch_words()
# print(result1)

# result2 = words.fetch_words()
# print(result2)

# ---------------------------------------------------
# from check.words import fetch_words
# from words import fetch_words

# result1 = fetch_words()
# print(result1)

# result2 = fetch_words()
# print(result2)

# ---------------------------------------------------
# from check.words import fetch_words as fw1
# from words import fetch_words as fw2

# result1 = fw1()
# print(result1)

# result2 = fw2()
# print(result2)

# ------------------------------------

# main.py

from my_utils import greet, add

print(greet("Manish"))  # Output: Hello, Manish!
print(add(5, 7))        # Output: 12
