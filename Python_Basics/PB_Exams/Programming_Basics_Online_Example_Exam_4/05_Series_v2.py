def calculate_series_budget(budget, series_count):
    total_cost = 0
    discounts = {
        'Thrones': 0.5,
        'Lucifer': 0.4,
        'Protector': 0.3,
        'TotalDrama': 0.2,
        'Area': 0.1,
    }

    for _ in range(series_count):
        series_name = input()
        series_price = float(input())
        if series_name in discounts:
            series_price *= (1 - discounts[series_name])
        total_cost += series_price

    if budget >= total_cost:
        remaining = budget - total_cost
        print(f'You bought all the series and left with {remaining:.2f} lv.')
    else:
        needed = total_cost - budget
        print(f'You need {needed:.2f} lv. more to buy the series!')


budget_input = float(input())
series_count_input = int(input())
calculate_series_budget(budget=budget_input, series_count=series_count_input)
