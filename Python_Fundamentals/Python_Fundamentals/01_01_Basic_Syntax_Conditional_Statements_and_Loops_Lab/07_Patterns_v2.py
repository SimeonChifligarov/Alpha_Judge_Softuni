def create_pattern(max_stars):
    for i in range(1, max_stars + 1):
        print('*' * i)
    for i in range(max_stars - 1, 0, -1):
        print('*' * i)


if __name__ == '__main__':
    max_stars_input = int(input())
    create_pattern(max_stars=max_stars_input)
