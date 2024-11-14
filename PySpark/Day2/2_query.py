# def greeting(language):
#     if language == "en":
#         return "Hello"
#     elif language == "es":
#         return "Hola"
#     elif language == "fr":
#         return "Bonjour"
#     else:
#         return "Hi"
    
# print(greeting("en"))  # Output: Hello
# print(greeting("es"))  # Output: Hola
# print(greeting("fr"))  # Output: Bonjour
# print(greeting("de"))  # Output: Hi

def greet_in(language):
    def get_greeting():
        greetings = {
            "en": "Hello",
            "es": "Hola",
            "fr": "Bonjour",
        }
        return greetings.get(language, "Hi")
    
    return get_greeting

print(greet_in("en")())  # Output: Hello
print(greet_in("es")())  # Output: Hola
print(greet_in("fr")())  # Output: Bonjour
print(greet_in("de")())  # Output: Hi