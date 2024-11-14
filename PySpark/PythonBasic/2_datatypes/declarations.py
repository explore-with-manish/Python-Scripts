"""Module to understand Mutable and Immutable"""

# a = 10
# print(a)
# print(type(a))
# print(id(a))

# b = a
# print(id(b))

# print("\nAfter Change")
# b = 20
# print(a)
# print(id(a))

# print(b)
# print(id(b))


arr = [1, 2, 3, 4]
# print(arr)
# print(id(arr))

# arr.append(5)
# print(arr)
# print(id(arr))


# def append(arr, item):
#     arr.append(item)
#     return tArr


# def append(source_arr, item):
#     """Method to append items to Array"""
#     temp_arr = source_arr[:]
#     temp_arr.append(item)
#     return temp_arr


def append(source_arr, item):
    """Method to append items to Array"""
    return [*source_arr, item]


arr1 = append(arr, 5)
print("Array1: ", arr1)

arr2 = append(arr, 5)
print("Array2: ", arr2)


# a, b, c = 10, 20.5, "BFL"
# a, b, c = 10, 20.5
# a = b = c = 10
