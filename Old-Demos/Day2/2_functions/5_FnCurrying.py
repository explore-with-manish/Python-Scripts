# Currying is a way of constructing functions that allows partial application of a function’s arguments.

# What this means is that you can pass all of the arguments a function is expecting and get the result,
# or pass a subset of those arguments and get a function back that’s waiting for the rest of the arguments.


# def greetings(msg, name):
#     return f"{msg}, {name}"


# print(greetings("Good Morning", "Manish"))
# print(greetings("Good Morning", "Abhijeet"))
# print(greetings("Good Morning", "Ramakant"))


# def converter(toUnit, factor, offset, inp):
#     return (str((offset+inp)*factor) + " " + toUnit)


# print(converter('km', 1.6, 0, 10))
# print(converter('km', 1.6, 0, 100))
# print(converter('km', 1.6, 0, 240))
# print(converter('km', 1.6, 0, 890))

# print(converter('INR', 71, 0, 10))
# print(converter('INR', 71, 0, 100))
# print(converter('INR', 71, 0, 240))
# print(converter('INR', 71, 0, 890))


# -----------------------------------------------------------------------------------------------

# def greetings(msg):
#     def greet(name):
#         return f"{msg}, {name}"
#     return greet


# mGreet = greetings("Good Morning")
# print(mGreet("Manish"))
# print(mGreet("Abhijeet"))
# print(mGreet("Ramakant"))

# aGreet = greetings("Good Afternoon")
# print(aGreet("Manish"))
# print(aGreet("Abhijeet"))
# print(aGreet("Ramakant"))

def get_converter(toUnit, factor, offset):
    def converter(inp):
        return (str((offset+inp)*factor) + " " + toUnit)
    return converter


milesToKm = get_converter('km', 1.6, 0)

print(milesToKm(10))
print(milesToKm(100))
print(milesToKm(240))
print(milesToKm(890))

usdToINR = get_converter('INR', 71, 0)

print(usdToINR(10))
print(usdToINR(100))
print(usdToINR(240))
print(usdToINR(890))

# print(get_converter('INR', 71, 0)(999))