def apply_discount(amount):
    return amount * 0.9

def filter_large_orders(amount):
    return amount if amount > 100 else None

def process_orders(orders, callback):
    result = []
    for order in orders:
        value = callback(order)
        if value is not None:
            result.append(value)
    return result

orders = [20, 200, 400, 50, 700]

print(process_orders(orders, apply_discount))

print(process_orders(orders, filter_large_orders))
