def bakery_rush(events: str) -> None:
    """
    Simulates a working day at a bakery with energy and coins management.
    """

    energy = 100
    coins = 100
    events_list = events.split('|')

    for event in events_list:
        name, value = event.split('-')
        value = int(value)

        if name == 'rest':
            gained_energy = min(100 - energy, value)
            energy += gained_energy
            print(f'You gained {gained_energy} energy.')
            print(f'Current energy: {energy}.')
        elif name == 'order':
            if energy >= 30:
                energy -= 30
                coins += value
                print(f'You earned {value} coins.')
            else:
                energy += 50
                print('You had to rest!')
        else:
            if coins >= value:
                coins -= value
                print(f'You bought {name}.')
            else:
                print(f'Closed! Cannot afford {name}.')
                return

    print('Day completed!')
    print(f'Coins: {coins}')
    print(f'Energy: {energy}')


if __name__ == '__main__':
    events_input = input()
    bakery_rush(events=events_input)
