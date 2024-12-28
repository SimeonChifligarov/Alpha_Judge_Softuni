def easter_egg_store(initial_eggs):
    sold_eggs = 0

    while True:
        command = input()
        if command == 'Close':
            result = [
                'Store is closed!',
                f'{sold_eggs} eggs sold.',
            ]

            return result

        quantity = int(input())

        if command == 'Buy':
            if quantity > initial_eggs:
                result = [
                    'Not enough eggs in store!',
                    f'You can buy only {initial_eggs}.',
                ]

                return result

            initial_eggs -= quantity
            sold_eggs += quantity
        elif command == 'Fill':
            initial_eggs += quantity


starting_eggs = int(input())

res = easter_egg_store(starting_eggs)
print('\n'.join(res))
