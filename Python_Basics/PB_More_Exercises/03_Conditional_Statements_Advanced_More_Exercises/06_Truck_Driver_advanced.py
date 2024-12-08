season = input()
km_per_month = float(input())

prices = {
    'Spring': {
        'km_up_to_5000': 0.75,
        'km_5001_to_10000': 0.95,
        'km_10001_to_20000': 1.45,
    },
    'Autumn': {
        'km_up_to_5000': 0.75,
        'km_5001_to_10000': 0.95,
        'km_10001_to_20000': 1.45,
    },
    'Summer': {
        'km_up_to_5000': 0.90,
        'km_5001_to_10000': 1.10,
        'km_10001_to_20000': 1.45,
    },
    'Winter': {
        'km_up_to_5000': 1.05,
        'km_5001_to_10000': 1.25,
        'km_10001_to_20000': 1.45,
    },
}

if km_per_month <= 5000:
    price_per_km = prices[season]['km_up_to_5000']
elif km_per_month <= 10000:
    price_per_km = prices[season]['km_5001_to_10000']
else:
    price_per_km = prices[season]['km_10001_to_20000']

monthly_salary = km_per_month * price_per_km * 4
salary_after_taxes = monthly_salary * 0.90

print(f'{salary_after_taxes:.2f}')
