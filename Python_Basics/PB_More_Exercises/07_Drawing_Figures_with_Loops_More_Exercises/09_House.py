def print_house(n):
    for i in range((n + 1) // 2):
        stars = '*' * (2 * i + 1 if n % 2 == 1 else 2 * i + 2)
        padding = '-' * ((n - len(stars)) // 2)
        print(padding + stars + padding)

    for _ in range(n // 2):
        print('|' + '*' * (n - 2) + '|')


n = int(input())

if 2 <= n <= 100:
    print_house(n)
else:
    raise ValueError('Please insert n value: 2 ≤ n ≤ 100.')
