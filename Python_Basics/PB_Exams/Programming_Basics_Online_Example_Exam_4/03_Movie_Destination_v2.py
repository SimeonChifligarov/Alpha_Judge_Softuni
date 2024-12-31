def calculate_film_cost(budget, destination, season, days):
    daily_prices = {
        'Winter': {'Dubai': 45_000, 'Sofia': 17_000, 'London': 24_000},
        'Summer': {'Dubai': 40_000, 'Sofia': 12_500, 'London': 20_250},
    }

    base_cost = daily_prices[season][destination] * days

    if destination == 'Dubai':
        total_cost = base_cost * 0.7
    elif destination == 'Sofia':
        total_cost = base_cost * 1.25
    else:
        total_cost = base_cost

    if budget >= total_cost:
        remaining_budget = budget - total_cost
        return f'The budget for the movie is enough! We have {remaining_budget:.2f} leva left!'
    else:
        needed_budget = total_cost - budget
        return f'The director needs {needed_budget:.2f} leva more!'


movie_budget = float(input())
movie_destination = input()
movie_season = input()
shooting_days = int(input())

result = calculate_film_cost(movie_budget, movie_destination, movie_season, shooting_days)
print(result)
