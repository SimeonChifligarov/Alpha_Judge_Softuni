budget = float(input())
fuel_needed = float(input())
day_of_week = input()

fuel_price_per_liter = 2.10
guide_price = 100

fuel_cost = fuel_needed * fuel_price_per_liter
total_cost = fuel_cost + guide_price

if day_of_week == 'Saturday':
    total_cost *= 0.90
elif day_of_week == 'Sunday':
    total_cost *= 0.80

if budget >= total_cost:
    money_left = budget - total_cost
    print(f'Safari time! Money left: {money_left:.2f} lv.')
else:
    money_needed = total_cost - budget
    print(f'Not enough money! Money needed: {money_needed:.2f} lv.')
