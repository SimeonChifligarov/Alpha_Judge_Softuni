fruit_prices_weekdays = {
    'banana': 2.50,
    'apple': 1.20,
    'orange': 0.85,
    'grapefruit': 1.45,
    'kiwi': 2.70,
    'pineapple': 5.50,
    'grapes': 3.85,
}

fruit_prices_weekend = {
    'banana': 2.70,
    'apple': 1.25,
    'orange': 0.90,
    'grapefruit': 1.60,
    'kiwi': 3.00,
    'pineapple': 5.60,
    'grapes': 4.20,
}

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
weekend = ['Saturday', 'Sunday']

fruit = input()
day = input()
quantity = float(input())

is_valid = True
prices = {}
if day in weekdays:
    prices = fruit_prices_weekdays
elif day in weekend:
    prices = fruit_prices_weekend
else:
    is_valid = False

if fruit not in fruit_prices_weekdays:
    is_valid = False

if is_valid:
    price = prices.get(fruit, 0)
    total_price = price * quantity
    print(f'{total_price:.2f}')
else:
    print('error')
