n = int(input())

print('*' * (2 * n) + ' ' * n + '*' * (2 * n))
for row in range(1, n - 1):
    if row == ((n - 1) // 2):
        print('*' + '/' * (2 * n - 2) + '*' + '|' * n + '*' + '/' * (2 * n - 2) + '*')
    else:
        print('*' + '/' * (2 * n - 2) + '*' + ' ' * n + '*' + '/' * (2 * n - 2) + '*')
print('*' * (2 * n) + ' ' * n + '*' * (2 * n))
