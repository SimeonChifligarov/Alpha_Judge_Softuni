def shopping_list(budget, **products):
    if budget < 100:
        return "You do not have enough budget."

    basket = []
    for product, (price, qty) in products.items():
        if len(basket) == 5:
            break
        total = price * qty
        if budget >= total:
            budget -= total
            basket.append(f"You bought {product} for {total:.2f} leva.")

    return "\n".join(basket)
