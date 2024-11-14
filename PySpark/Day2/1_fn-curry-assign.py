def apply_discount(category):
    def product(name):
        def discount(percentage):
            if percentage>50:
                return "Discount above 50% is not allowed."
            return f"Applied {percentage}% discount on {name} in {category} category."
        return discount
    return product

print(apply_discount("Clothing")("T-shirt")(20))
print(apply_discount("Electronics")("Samartphone")(55))