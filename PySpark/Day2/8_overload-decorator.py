def overload(func):
    registry = {}

    def dispatcher(*args, **kwargs):
        key = (len(args), tuple(type(arg) for arg in args))
        if key in registry:
            return registry[key](*args, **kwargs)
        else:
            raise Exception("No Implemenattion Found")
    
    def register(*arg_types):
        def wrapper(f):
            key = (len(arg_types), arg_types)
            # print(key)
            registry[key] = f
            return dispatcher
        return wrapper

    dispatcher.register = register
    return dispatcher

@overload
def add():
    pass

@add.register(int, int)
def add_two_numbers(a,b):
    return a+b

@add.register(int, int, int)
def add_three_numbers(a,b,c):
    return a+b+c

@add.register(float, float)
def add_two_float(a,b):
    return a+b

print(add(2,3))
print(add(2,3,4))
print(add(2.5,3.6))
