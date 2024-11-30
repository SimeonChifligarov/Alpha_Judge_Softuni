destination = input()

while destination != 'End':
    budget = float(input())
    saved_money = 0

    while saved_money < budget:
        amount = float(input())
        saved_money += amount

    print(f'Going to {destination}!')
    destination = input()
