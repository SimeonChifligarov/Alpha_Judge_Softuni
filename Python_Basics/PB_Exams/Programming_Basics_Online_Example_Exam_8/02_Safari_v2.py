def calculate_safari_cost(budget, fuel_amount, day):
    fuel_rate = 2.10
    guide_fee = 100
    fuel_expense = fuel_amount * fuel_rate
    total_expense = fuel_expense + guide_fee

    if day == 'Saturday':
        total_expense *= 0.90
    elif day == 'Sunday':
        total_expense *= 0.80

    if budget >= total_expense:
        return f'Safari time! Money left: {(budget - total_expense):.2f} lv.'
    else:
        return f'Not enough money! Money needed: {(total_expense - budget):.2f} lv.'


if __name__ == '__main__':
    available_budget = float(input())
    liters_needed = float(input())
    travel_day = input()
    result = calculate_safari_cost(budget=available_budget, fuel_amount=liters_needed, day=travel_day)
    print(result)
