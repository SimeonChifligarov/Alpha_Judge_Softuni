import math


def easter_budget_calculation(guests_count, available_budget):
    easter_bread_price = 4
    egg_price = 0.45

    needed_breads = math.ceil(guests_count / 3)
    needed_eggs = guests_count * 2

    total_cost = (needed_breads * easter_bread_price) + (needed_eggs * egg_price)

    if available_budget >= total_cost:
        remaining_money = available_budget - total_cost
        print(f'Lyubo bought {needed_breads} Easter bread and {needed_eggs} eggs.')
        print(f'He has {remaining_money:.2f} lv. left.')
    else:
        money_short = total_cost - available_budget
        print('Lyubo doesn\'t have enough money.')
        print(f'He needs {money_short:.2f} lv. more.')


guests = int(input())
budget = int(input())

easter_budget_calculation(guests, budget)
