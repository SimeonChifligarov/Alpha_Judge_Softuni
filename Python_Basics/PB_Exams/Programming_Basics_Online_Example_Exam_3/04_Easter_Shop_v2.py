def easter_egg_store(initial_eggs):
    sold_eggs = 0

    while True:
        command = input()
        if command == 'Close':
            print('Store is closed!')
            print(f'{sold_eggs} eggs sold.')
            break

        quantity = int(input())

        if command == 'Buy':
            if quantity > initial_eggs:
                print('Not enough eggs in store!')
                print(f'You can buy only {initial_eggs}.')
                break
            initial_eggs -= quantity
            sold_eggs += quantity
        elif command == 'Fill':
            initial_eggs += quantity


starting_eggs = int(input())

easter_egg_store(starting_eggs)
