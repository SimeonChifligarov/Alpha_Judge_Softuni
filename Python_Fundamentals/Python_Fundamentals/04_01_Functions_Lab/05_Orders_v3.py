def calculate_total_price(product: str, quantity: int) -> float:
    """
    Calculates the total price of an order based on the product and quantity.
    """
    prices = {
        'coffee': 1.50,
        'water': 1.00,
        'coke': 1.40,
        'snacks': 2.00,
    }
    result = prices.get(product, 0) * quantity
    return result


if __name__ == '__main__':
    product_input = input()
    quantity_input = int(input())
    total_price = calculate_total_price(product=product_input, quantity=quantity_input)
    print(f'{total_price:.2f}')
