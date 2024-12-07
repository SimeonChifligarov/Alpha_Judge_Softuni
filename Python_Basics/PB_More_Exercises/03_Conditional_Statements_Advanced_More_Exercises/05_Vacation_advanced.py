budget = float(input())
season = input()

pricing = {
    'Camp': {
        'Summer': {'location': 'Alaska', 'percent': 0.65},
        'Winter': {'location': 'Morocco', 'percent': 0.45},
    },
    'Hut': {
        'Summer': {'location': 'Alaska', 'percent': 0.80},
        'Winter': {'location': 'Morocco', 'percent': 0.60},
    },
    'Hotel': {
        'Summer': {'location': 'Alaska', 'percent': 0.90},
        'Winter': {'location': 'Morocco', 'percent': 0.90},
    },
}

if budget <= 1000:
    accommodation = 'Camp'
elif 1000 < budget <= 3000:
    accommodation = 'Hut'
else:
    accommodation = 'Hotel'

location = pricing[accommodation][season]['location']
price_percentage = pricing[accommodation][season]['percent']
price = budget * price_percentage

print(f'{location} - {accommodation} - {price:.2f}')
