# def convert(s):
#     x = int(s)
#     return x

# print(convert("10"))
# print(type(convert("10")))

# print(convert("ab"))
# print("I am the last line")

# -------------------------------------------


# def convert(s):
#     try:
#         x = int(s)
#         print("Coversion Success")
#     except ValueError:
#         x = -1
#         print("Coversion Failed")
#     except TypeError:
#         x = -1
#         print("Coversion Failed")

#     return x

# def convert(s):
#     try:
#         x = int(s)
#         print("Coversion Success")
#     except (ValueError, TypeError) as e:
#         x = -1
#         print(str(e))

#     return x

# def convert(s):
#     try:
#         x = int(s)
#         print("Coversion Success")
#     except Exception as e:
#         x = -1
#         print(str(e))

#     return x

# def convert(s):
#     try:
#         x = int(s)
#         print("Coversion Success")
#     except:
#         x = -1
#         print("Error")

#     return x

def convert(s):
    try:
        x = int(s)
    except:
        raise Exception("Error Converting Value")

    return x


# try:
#     print(convert("10"))
#     print(convert("ab"))
#     print(convert(list()))
#     print(convert("-1"))
#     print("I am the last line")
# except Exception as e:
#     print(str(e))


try:
    print(convert("10"))
except Exception as e:
    print(str(e))


try:
    print(convert("ab"))
except Exception as e:
    print(str(e))

try:
    print(convert(list()))
except Exception as e:
    print(str(e))
finally:
    print("I am Finally block")
    
try:
    print(convert("-1"))
except Exception as e:
    print(str(e))
finally:
    print("I am Finally block")