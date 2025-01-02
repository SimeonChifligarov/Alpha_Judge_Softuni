def calculate_order(drink, sugar, quantity):
    prices = {
        'Espresso': {'Without': 0.90, 'Normal': 1.00, 'Extra': 1.20},
        'Cappuccino': {'Without': 1.00, 'Normal': 1.20, 'Extra': 1.60},
        'Tea': {'Without': 0.50, 'Normal': 0.60, 'Extra': 0.70},
    }

    price_per_cup = prices[drink][sugar]
    total_price = price_per_cup * quantity

    if sugar == 'Without':
        total_price *= 0.65
    if drink == 'Espresso' and quantity >= 5:
        total_price *= 0.75
    if total_price > 15:
        total_price *= 0.80

    print(f'You bought {quantity} cups of {drink} for {total_price:.2f} lv.')


beverage = input()
sugar_level = input()
cups = int(input())

calculate_order(drink=beverage, sugar=sugar_level, quantity=cups)
