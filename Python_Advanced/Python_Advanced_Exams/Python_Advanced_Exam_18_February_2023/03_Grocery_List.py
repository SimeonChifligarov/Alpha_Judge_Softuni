def shop_from_grocery_list(budget, grocery_list, *products):
    bought = set()
    needed = list(grocery_list)
    for name, price in products:
        if name not in needed or name in bought:
            continue
        if budget < price:
            break
        budget -= price
        bought.add(name)
    missing = [item for item in needed if item not in bought]

    if not missing:
        return f"Shopping is successful. Remaining budget: {budget:.2f}."
    return f"You did not buy all the products. Missing products: {', '.join(missing)}."
