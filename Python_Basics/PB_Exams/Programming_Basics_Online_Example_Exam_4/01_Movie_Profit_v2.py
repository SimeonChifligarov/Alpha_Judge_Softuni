def calculate_profit(movie_name, days, tickets_per_day, ticket_price, cinema_percentage):
    total_income = days * tickets_per_day * ticket_price
    studio_profit = total_income * (1 - cinema_percentage / 100)
    return studio_profit


movie = input()
days_count = int(input())
tickets_count = int(input())
price_per_ticket = float(input())
cinema_share = int(input())


profit = calculate_profit(movie, days_count, tickets_count, price_per_ticket, cinema_share)
print(f'The profit from the movie {movie} is {profit:.2f} lv.')
