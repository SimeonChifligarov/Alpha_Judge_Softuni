def vacation_budget(budget, nights, night_price, additional_percentage):
    nights_cost = nights * night_price
    if nights > 7:
        nights_cost *= 0.95
    additional_costs = budget * (additional_percentage / 100)
    total_cost = nights_cost + additional_costs
    budget_left = budget - total_cost
    if budget_left >= 0:
        print(f'Ivanovi will be left with {budget_left:.2f} leva after vacation.')
    else:
        print(f'{-budget_left:.2f} leva needed.')


available_budget = float(input())
planned_nights = int(input())
cost_per_night = float(input())
extra_percentage = int(input())
vacation_budget(available_budget, planned_nights, cost_per_night, extra_percentage)
