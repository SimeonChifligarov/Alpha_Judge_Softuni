flower_type = input()
flower_count = int(input())
budget = int(input())

flower_prices = {
    'Roses': 5.00,
    'Dahlias': 3.80,
    'Tulips': 2.80,
    'Narcissus': 3.00,
    'Gladiolus': 2.50,
}

price = flower_prices[flower_type]
discount = 0

if flower_type == 'Roses' and flower_count > 80:
    discount = 0.10
elif flower_type == 'Dahlias' and flower_count > 90:
    discount = 0.15
elif flower_type == 'Tulips' and flower_count > 80:
    discount = 0.15
elif flower_type == 'Narcissus' and flower_count < 120:
    discount = -0.15
elif flower_type == 'Gladiolus' and flower_count < 80:
    discount = -0.20

total_price = price * flower_count * (1 - discount)

if budget >= total_price:
    remaining_budget = budget - total_price
    print(f'Hey, you have a great garden with {flower_count} {flower_type} and {remaining_budget:.2f} leva left.')
else:
    needed_money = total_price - budget
    print(f'Not enough money, you need {needed_money:.2f} leva more.')
