budget = float(input())
extras_count = int(input())
clothing_price_per_extra = float(input())

decor_price = budget * 0.10
clothing_total_price = extras_count * clothing_price_per_extra

if extras_count > 150:
    clothing_total_price *= 0.90

total_expenses = decor_price + clothing_total_price

if total_expenses > budget:
    money_needed = total_expenses - budget
    print('Not enough money!')
    print(f'Wingard needs {money_needed:.2f} leva more.')
else:
    remaining_money = budget - total_expenses
    print('Action!')
    print(f'Wingard starts filming with {remaining_money:.2f} leva left.')
