def cinema_simulation(capacity):
    total_income = 0
    seats_left = capacity

    while True:
        command = input()
        if command == 'Movie time!':
            print(f'There are {seats_left} seats left in the cinema.')
            break

        people = int(command)
        if people > seats_left:
            print('The cinema is full.')
            break

        seats_left -= people
        income = people * 5
        if people % 3 == 0:
            income -= 5

        total_income += income

    print(f'Cinema income - {total_income} lv.')


cinema_capacity = int(input())
cinema_simulation(cinema_capacity)
