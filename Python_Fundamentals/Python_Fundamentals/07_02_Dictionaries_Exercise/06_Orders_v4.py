from collections import defaultdict


def read_products() -> dict[str, dict[str, float | int]]:
    """
    Reads product data from input and stores product details using defaultdict.
    Returns a dictionary containing product names as keys and their price and quantity as values.
    """
    products = defaultdict(lambda: {'price': 0.0, 'quantity': 0})

    while True:
        data = input()
        if data == 'buy':
            break

        product_name, price, quantity = data.split()
        price, quantity = float(price), int(quantity)

        products[product_name]['quantity'] += quantity
        products[product_name]['price'] = price

    return products


def print_products(products: dict[str, dict[str, float | int]]) -> None:
    """
    Prints each product's name and total price, formatted to 2 decimal places.
    """
    for name, details in products.items():
        total_price = details['price'] * details['quantity']
        print(f'{name} -> {total_price:.2f}')


if __name__ == '__main__':
    product_data = read_products()
    print_products(products=product_data)
