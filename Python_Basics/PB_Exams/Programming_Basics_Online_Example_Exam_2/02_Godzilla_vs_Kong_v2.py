def film_budget_check(total_budget, num_extras, clothing_price_per_extra):
    decor_cost = total_budget * 0.1
    clothing_cost = num_extras * clothing_price_per_extra

    if num_extras > 150:
        clothing_cost *= 0.9

    total_cost = decor_cost + clothing_cost

    if total_cost > total_budget:
        deficit = total_cost - total_budget
        return f'Not enough money!\nWingard needs {deficit:.2f} leva more.'
    else:
        remaining = total_budget - total_cost
        return f'Action!\nWingard starts filming with {remaining:.2f} leva left.'


budget = float(input())
extras = int(input())
clothing_price = float(input())
print(film_budget_check(budget, extras, clothing_price))
