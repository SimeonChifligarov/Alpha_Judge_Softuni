budget = int(input())
season = input()
fishermen_count = int(input())

prices = {
    'Spring': 3000,
    'Summer': 4200,
    'Autumn': 4200,
    'Winter': 2600,
}

boat_price = prices[season]

if fishermen_count <= 6:
    discount = 0.10
elif fishermen_count <= 11:
    discount = 0.15
else:
    discount = 0.25

extra_discount = 0.05 if fishermen_count % 2 == 0 and season != 'Autumn' else 0

total_price = boat_price * (1 - discount) * (1 - extra_discount)

if budget >= total_price:
    remaining_money = budget - total_price
    print(f'Yes! You have {remaining_money:.2f} leva left.')
else:
    needed_money = total_price - budget
    print(f'Not enough money! You need {needed_money:.2f} leva.')
