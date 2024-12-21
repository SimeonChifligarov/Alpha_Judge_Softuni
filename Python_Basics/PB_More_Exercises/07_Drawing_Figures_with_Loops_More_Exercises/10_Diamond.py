import math


def print_diamond(n):
    starting_stars = 2 if n % 2 == 0 else 1
    upper_rows = math.ceil(n / 2) - 1
    lower_rows = []

    outer_dashes_count = (n - 1) // 2
    for i in range(upper_rows):
        outer_dashes = '-' * outer_dashes_count
        if i == 0:
            stars = '*' * starting_stars
        else:
            stars = '*' + '-' * (n - outer_dashes_count * 2 - 2) + '*'
        current_row = outer_dashes + stars + outer_dashes
        print(current_row)
        lower_rows.append(current_row)
        outer_dashes_count -= 1

    if n == 1:
        print('*')
    else:
        print('*' + '-' * (n - 2) + '*')

    print('\n'.join(lower_rows[::-1]))


size = int(input())

if 1 <= size <= 100:
    print_diamond(size)
else:
    raise ValueError('Please insert n value: 1 ≤ n ≤ 100.')
