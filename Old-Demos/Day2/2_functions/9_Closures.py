# ----------------------------------------
# A closure—unlike a plain function—allows the function to access those captured
# variables through the closure’s copies of their values or references, even when the
# function is invoked outside their scope.

# count = 0


# def next():
#     global count
#     count = count+1
#     return count


# print(next())
# print(next())
# count = "ABC"
# print(next())

# ---------------------------------------------------

# def get_next():
#     count = 0

#     def inc():
#         nonlocal count
#         count = count+1
#         return count

#     return inc

# next = get_next()

# print(next())
# print(next())
# count = "ABC"
# print(next())

# -----------------------------------------

def get_next(by):
    count = 0

    def inc():
        nonlocal count
        count = count+by
        return count

    return inc

next1 = get_next(1)

print(next1())
print(next1())
print(next1())

next5 = get_next(5)

print(next5())
print(next5())
print(next5())