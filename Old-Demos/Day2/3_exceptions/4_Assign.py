def add(a, b):
    if(isinstance(a, (int, float)) and isinstance(b, (int, float))):
        return a+b

    raise ValueError("Error: Arguments should be numeric")

try:
    print(add(2, 3))
    print(add(2, "xyz"))            # Error: Arguments should be numeric
except Exception as e:
    print(e)
