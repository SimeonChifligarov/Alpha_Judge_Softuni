number = int(input())

# print('\n'.join(str(2 ** power) for power in range(0, number + 1, 2)))

[print(2 ** power) for power in range(0, number + 1, 2)]
