# def greetings(msg, name):
#     return f"{msg}, {name}"

# print(greetings("Good Afternoon", "Manish"))
# print(greetings("Good Afternoon", "Abhijeet"))
# print(greetings("Good Afternoon", "Ramakant"))

# def converter(toUnit, factor, offset, inp):
#     return (str((offset+inp)*factor) + " " + toUnit)

# print(converter('km', 1.6, 0, 10))
# print(converter('km', 1.6, 0, 100))
# print(converter('km', 1.6, 0, 210))
# print(converter('km', 1.6, 0, 890))

# ----------------------------

def greetings(msg):
    def greet(name):
        return f"{msg}, {name}"
    return greet

mGreet = greetings("Good Morning")
print(mGreet("Manish"))
print(mGreet("Abhijeet"))
print(mGreet("Ramakant"))

aGreet = greetings("Good Afternoon")
print(aGreet("Manish"))
print(aGreet("Abhijeet"))
print(aGreet("Ramakant"))

def get_converter(toUnit, factor, offset):
    def converter(inp):
        return (str((offset+inp)*factor) + " " + toUnit)
    return converter

milesToKm = get_converter('km', 1.6, 0)

print(milesToKm(10))
print(milesToKm(100))
print(milesToKm(240))
print(milesToKm(890))

usdToINR = get_converter('INR', 83, 0)

print(usdToINR(10))
print(usdToINR(100))
print(usdToINR(240))
print(usdToINR(890))