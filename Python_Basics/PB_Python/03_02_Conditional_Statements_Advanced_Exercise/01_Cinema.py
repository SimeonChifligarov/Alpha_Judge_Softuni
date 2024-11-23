projection_type = input()
rows = int(input())
columns = int(input())

prices = {
    'Premiere': 12.00,
    'Normal': 7.50,
    'Discount': 5.00,
}

capacity = rows * columns
income = capacity * prices.get(projection_type, -1)

if income >= 0:
    print(f'{income:.2f}')
else:
    print('Invalid inputs')
    exit(5)
