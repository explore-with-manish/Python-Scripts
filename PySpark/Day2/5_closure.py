# count = 0

# def next():
#     global count
#     count = count+1
#     return count

# print(next())
# print(next())
# count = "ABC"
# print(next())

# # -------------------------------

# def next():
#     count = 0
#     count = count+1
#     return count

# print(next())
# print(next())
# count = "ABC"
# print(next())

# -------------------------------

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

# -------------------------------

def create_counter():
    count = 0
    
    def inc():
        nonlocal count
        count = count+1
        return count
    
    def dec():
        nonlocal count
        count = count-1
        return count
    
    return {'inc': inc, 'dec':dec}

counter = create_counter()

print(counter['inc']())
print(counter['inc']())
print(counter['dec']())
print(counter['dec']())