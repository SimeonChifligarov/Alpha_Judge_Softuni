def calculate_club_income(target_profit):
    total_income = 0

    while total_income < target_profit:
        cocktail_name = input()
        if cocktail_name == 'Party!':
            print(f'We need {target_profit - total_income:.2f} leva more.')
            break

        cocktail_count = int(input())
        price_per_cocktail = len(cocktail_name)
        order_price = price_per_cocktail * cocktail_count

        if order_price % 2 != 0:
            order_price *= 0.75

        total_income += order_price

    if total_income >= target_profit:
        print('Target acquired.')
    print(f'Club income - {total_income:.2f} leva.')


desired_profit = float(input())
calculate_club_income(target_profit=desired_profit)
