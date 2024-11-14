from functools import wraps

def overload(func):
    registry = {}

    def dispatcher(*args, **kwargs):
        """Dispatcher function to select the correct overload."""
        key = (len(args), tuple(type(arg) for arg in args))
        if key in registry:
            return registry[key](*args, **kwargs)
        else:
            raise TypeError(f"No matching function for arguments: {args}")

    def register(*arg_types):
        """Register a new overload with specific argument types."""
        def wrapper(f):
            key = (len(arg_types), arg_types)
            registry[key] = f
            return dispatcher  # Return dispatcher to allow chaining
        return wrapper

    dispatcher.register = register
    return dispatcher

# Usage Example
@overload
def add():
    pass  # Placeholder for overload registration

@add.register(int, int)
def add_two_integers(a, b):
    return a + b

@add.register(int, int, int)
def add_three_integers(a, b, c):
    return a + b + c

# Calling the overloaded functions
print(add(2, 3))            # Output: 5
print(add(1, 2, 3))         # Output: 6
