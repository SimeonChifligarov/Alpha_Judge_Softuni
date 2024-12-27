def calculate_easter_bakery_cost(flour_price_per_kg, flour_kg, sugar_kg, egg_cartons, yeast_packs):
    sugar_price_per_kg = flour_price_per_kg * 0.75
    egg_carton_price = flour_price_per_kg * 1.10
    yeast_pack_price = sugar_price_per_kg * 0.20

    flour_cost = flour_kg * flour_price_per_kg
    sugar_cost = sugar_kg * sugar_price_per_kg
    eggs_cost = egg_cartons * egg_carton_price
    yeast_cost = yeast_packs * yeast_pack_price

    total_cost = flour_cost + sugar_cost + eggs_cost + yeast_cost
    return f'{total_cost:.2f}'


flour_price = float(input())
flour_kg = float(input())
sugar_kg = float(input())
egg_cartons = int(input())
yeast_packs = int(input())

print(calculate_easter_bakery_cost(flour_price, flour_kg, sugar_kg, egg_cartons, yeast_packs))
