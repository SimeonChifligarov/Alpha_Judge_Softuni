def calculate_loaves(budget, flour_price):
    eggs_price = flour_price * 0.75
    milk_price_per_liter = flour_price * 1.25
    milk_price = milk_price_per_liter / 4
    loaf_cost = eggs_price + flour_price + milk_price
    loaves = 0
    colored_eggs = 0

    while budget >= loaf_cost:
        budget -= loaf_cost
        loaves += 1
        colored_eggs += 3
        if loaves % 3 == 0:
            colored_eggs -= (loaves - 2)

    return loaves, colored_eggs, budget


if __name__ == '__main__':
    total_budget = float(input())
    price_per_flour = float(input())
    result_loaves, result_eggs, result_money = calculate_loaves(budget=total_budget, flour_price=price_per_flour)
    print(
        f'You made {result_loaves} loaves of Easter bread! Now you have {result_eggs} eggs'
        f' and {result_money:.2f}BGN left.'
    )
