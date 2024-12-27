def calculate_easter_lunch_cost(cozonacs, egg_cartons, cookies_kg):
    prices = {
        'cozonac': 3.20,
        'egg_carton': 4.35,
        'cookie_kg': 5.40,
        'egg_paint': 0.15,
    }

    cozonacs_cost = cozonacs * prices['cozonac']
    eggs_cost = egg_cartons * prices['egg_carton']
    paint_cost = egg_cartons * 12 * prices['egg_paint']
    cookies_cost = cookies_kg * prices['cookie_kg']

    total_cost = cozonacs_cost + eggs_cost + paint_cost + cookies_cost
    return f'{total_cost:.2f}'


cozonacs_count = int(input())
egg_cartons_count = int(input())
cookies_kg_count = int(input())
print(calculate_easter_lunch_cost(cozonacs_count, egg_cartons_count, cookies_kg_count))
