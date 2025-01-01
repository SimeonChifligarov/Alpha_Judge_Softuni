def best_movie():
    max_movies = 7
    best_film = ''
    best_score = float('-inf')
    count = 0

    while count < max_movies:
        movie_title = input()
        if movie_title == 'STOP':
            break

        count += 1
        ascii_sum = sum(ord(char) for char in movie_title)
        length = len(movie_title)

        for char in movie_title:
            if char.islower():
                ascii_sum -= 2 * length
            elif char.isupper():
                ascii_sum -= length

        if ascii_sum > best_score:
            best_score = ascii_sum
            best_film = movie_title

    if count == max_movies:
        print('The limit is reached.')
    print(f'The best movie for you is {best_film} with {best_score} ASCII sum.')


if __name__ == '__main__':
    best_movie()
