def manage_budget(budget):
    while True:
        command = input()
        if command == 'End':
            print('You bought everything needed.')
            break

        price = int(command)
        if price > budget:
            print('You went in overdraft!')
            break
        budget -= price


if __name__ == '__main__':
    budget_input = int(input())
    manage_budget(budget=budget_input)
