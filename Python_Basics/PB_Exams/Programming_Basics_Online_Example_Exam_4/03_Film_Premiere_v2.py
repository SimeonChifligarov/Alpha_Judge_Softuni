def calculate_bill(movie, package, tickets):
    prices = {
        'John Wick': {'Drink': 12, 'Popcorn': 15, 'Menu': 19},
        'Star Wars': {'Drink': 18, 'Popcorn': 25, 'Menu': 30},
        'Jumanji': {'Drink': 9, 'Popcorn': 11, 'Menu': 14},
    }

    price_per_ticket = prices[movie][package]
    total_price = price_per_ticket * tickets

    if movie == 'Star Wars' and tickets >= 4:
        total_price *= 0.7
    elif movie == 'Jumanji' and tickets == 2:
        total_price *= 0.85

    return total_price


movie_name = input()
package_type = input()
ticket_count = int(input())

final_price = calculate_bill(movie_name, package_type, ticket_count)
print(f'Your bill is {final_price:.2f} leva.')
