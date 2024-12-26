def analyze_movie_ratings(num_movies):
    highest_rating = float('-inf')
    lowest_rating = float('inf')
    total_rating = 0
    highest_rated_movie = ''
    lowest_rated_movie = ''

    for _ in range(num_movies):
        movie_name = input()
        rating = float(input())
        total_rating += rating

        if rating > highest_rating:
            highest_rating = rating
            highest_rated_movie = movie_name
        if rating < lowest_rating:
            lowest_rating = rating
            lowest_rated_movie = movie_name

    average_rating = total_rating / num_movies

    result = [
        f'{highest_rated_movie} is with highest rating: {highest_rating:.1f}',
        f'{lowest_rated_movie} is with lowest rating: {lowest_rating:.1f}',
        f'Average rating: {average_rating:.1f}',
    ]

    return result


movies_count = int(input())

res = analyze_movie_ratings(movies_count)
print('\n'.join(res))
