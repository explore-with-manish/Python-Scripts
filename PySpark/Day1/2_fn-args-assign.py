def place_order(customer_name, order_id, *items, delivery_charge=50, **details):
# def place_order(customer_name, order_id, delivery_charge=50, *items,  **details):
    print(f"Order Summary for {customer_name} (Order ID: {order_id}):")

    # print(type(items))

    # for item in items:
    #     print(type(item))
    
    total=0
    for item_name, price in items:
        print(f"- {item_name}: {price} INR")
        total += price

    print(f"Delivery Charge: {delivery_charge} INR")
    total += delivery_charge

    if details: 
        print("\nAdditional Details:")
        for key, value in details.items():
            print(f"{key}: {value}")

    print(f"\nTotal Amount: {total} INR")

place_order("Manish", 1001, 100, 
            ("Pizza", 300),
            ("Pasta", 200),
            ("Coke", 50),
            coupon="FREEDELIVERY",
            delivery_instructions="Leave at the main door")

# place_order("Manish", 1001,  
#             ("Pizza", 300),
#             ("Pasta", 200),
#             ("Coke", 50),
#             coupon="FREEDELIVERY",
#             delivery_instructions="Leave at the main door")

    