def manage_products() -> None:
    """
    Manages products by storing their prices and quantities.
    Updates price if it changes and accumulates quantity.
    Prints the total price for each product upon receiving 'buy' command.
    """
    products = {}

    while True:
        data = input()
        if data == 'buy':
            break

        name, price, quantity = data.split()
        price, quantity = float(price), int(quantity)

        if name in products:
            products[name]['quantity'] += quantity
            products[name]['price'] = price
        else:
            products[name] = {'price': price, 'quantity': quantity}

    for name, details in products.items():
        total_price = details['price'] * details['quantity']
        print(f'{name} -> {total_price:.2f}')


if __name__ == '__main__':
    manage_products()
