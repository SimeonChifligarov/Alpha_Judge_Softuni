# using while True

needed_money = float(input())
available_money = float(input())

days_count = 0
spend_days = 0

while True:
    action = input()
    amount = float(input())
    days_count += 1

    if action == 'spend':
        spend_days += 1
        available_money -= amount
        if available_money < 0:
            available_money = 0
        if spend_days == 5:
            print('You can\'t save the money.')
            print(days_count)
            break
    elif action == 'save':
        spend_days = 0
        available_money += amount

    if available_money >= needed_money:
        print(f'You saved the money for {days_count} days.')
        break
