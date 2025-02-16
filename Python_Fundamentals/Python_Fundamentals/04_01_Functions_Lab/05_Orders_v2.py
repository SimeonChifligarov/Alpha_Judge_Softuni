def total_price_of_order(order_type, order_quantity):
    prices = {
        'coffee': 1.50,
        'water': 1.00,
        'coke': 1.40,
        'snacks': 2.00,
    }
    return order_quantity * prices.get(order_type, 0)  # default price=0


product = input()
quantity = int(input())
total_price_output = total_price_of_order(product, quantity)
print(f'{total_price_output:.2f}')
