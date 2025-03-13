from collections import defaultdict


def process_products() -> None:
    """
    Reads product data from input, stores product details using defaultdict,
    and prints the total price per product.
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

    for name, details in products.items():
        total_price = details['price'] * details['quantity']
        print(f'{name} -> {total_price:.2f}')


if __name__ == '__main__':
    process_products()
