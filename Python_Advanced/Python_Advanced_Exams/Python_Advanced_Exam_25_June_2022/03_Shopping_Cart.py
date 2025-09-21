def shopping_cart(*args):
    limits = {"Soup": 3, "Pizza": 4, "Dessert": 2}
    cart = {"Soup": [], "Pizza": [], "Dessert": []}

    for item in args:
        if item == "Stop":
            break
        meal, product = item
        if len(cart[meal]) < limits[meal] and product not in cart[meal]:
            cart[meal].append(product)

    if not any(cart.values()):
        return "No products in the cart!"

    sorted_cart = sorted(cart.items(), key=lambda x: (-len(x[1]), x[0]))
    result = []
    for meal, products in sorted_cart:
        result.append(f"{meal}:")
        for product in sorted(products):
            result.append(f" - {product}")

    return "\n".join(result)
