# using while True

total_sum = 0

while True:
    command = input()
    if command == 'NoMoreMoney':
        break

    amount = float(command)
    if amount < 0:
        print('Invalid operation!')
        break

    print(f'Increase: {amount:.2f}')
    total_sum += amount

print(f'Total: {total_sum:.2f}')
