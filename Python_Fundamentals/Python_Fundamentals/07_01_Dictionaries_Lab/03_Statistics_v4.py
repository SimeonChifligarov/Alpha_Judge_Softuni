from collections import defaultdict


def process_inventory() -> None:
    """Processes inventory input and prints the final statistics."""
    inventory = defaultdict(int)

    while True:
        data = input()
        if data == 'statistics':
            break
        product, quantity = data.split(': ')
        inventory[product] += int(quantity)

    print('Products in stock:')
    for product, quantity in inventory.items():
        print(f'- {product}: {quantity}')

    print(f'Total Products: {len(inventory)}')
    print(f'Total Quantity: {sum(inventory.values())}')


if __name__ == '__main__':
    process_inventory()
