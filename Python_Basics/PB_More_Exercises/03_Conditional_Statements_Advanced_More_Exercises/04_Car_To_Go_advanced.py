budget = float(input())
season = input()

pricing = {
    'Economy class': {
        'Summer': {
            'type': 'Cabrio',
            'percent': 0.35,
        },
        'Winter': {
            'type': 'Jeep',
            'percent': 0.65,
        },
    },
    'Compact class': {
        'Summer': {
            'type': 'Cabrio',
            'percent': 0.45,
        },
        'Winter': {
            'type': 'Jeep',
            'percent': 0.80,
        },
    },
    'Luxury class': {
        'Summer': {
            'type': 'Jeep',
            'percent': 0.90,
        },
        'Winter': {
            'type': 'Jeep',
            'percent': 0.90,
        },
    },
}

if budget <= 100:
    car_class = 'Economy class'
elif 100 < budget <= 500:
    car_class = 'Compact class'
else:
    car_class = 'Luxury class'

car_type = pricing[car_class][season]['type']
price_percentage = pricing[car_class][season]['percent']
price = budget * price_percentage

print(f'{car_class}')
print(f'{car_type} - {price:.2f}')
