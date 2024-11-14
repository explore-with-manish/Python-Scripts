import time
from functools import wraps

def rate_limiter(max_calls, period):
    """
    A decorator to enforce a rate limit on a function.
    
    :param max_calls: Maximum number of calls allowed within the time window.
    :param period: Time window (in seconds) for the allowed calls.
    """
    timestamps = []  # Store the timestamps of function calls

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            now = time.time()

            # Remove timestamps older than the allowed period
            while timestamps and now - timestamps[0] >= period:
                timestamps.pop(0)

            # Check if the function call exceeds the limit
            if len(timestamps) >= max_calls:
                return "Rate limit exceeded, please try again later."

            # Log the call and proceed
            timestamps.append(now)
            return func(*args, **kwargs)

        return wrapper

    return decorator

# Example Usage
@rate_limiter(max_calls=3, period=10)  # Allow 3 calls every 10 seconds
def place_order(order_id):
    return f"Order {order_id} placed successfully."

@rate_limiter(max_calls=2, period=5)  # Allow 2 calls every 5 seconds
def manage_account(user_id):
    return f"Account {user_id} managed successfully."

# Test Calls
print(place_order(1))  # Output: Order 1 placed successfully.
print(place_order(2))  # Output: Order 2 placed successfully.
print(place_order(3))  # Output: Order 3 placed successfully.
print(place_order(4))  # Output: Rate limit exceeded, please try again later.

print("System Cooling Down")
time.sleep(10)  # Wait for the cooldown period

print(place_order(5))  # Output: Order 5 placed successfully.
print(manage_account(100))  # Output: Account 100 managed successfully.
print(manage_account(101))  # Output: Account 101 managed successfully.
print(manage_account(102))  # Output: Rate limit exceeded, please try again later.
