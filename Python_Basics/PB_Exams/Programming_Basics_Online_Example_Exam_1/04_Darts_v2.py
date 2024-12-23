def dart_game(player_name):
    starting_points = 301
    successful_shots = 0
    unsuccessful_shots = 0

    while True:
        command = input()
        if command == 'Retire':
            print(f'{player_name} retired after {unsuccessful_shots} unsuccessful shots.')
            break

        sector = command
        points = int(input())

        score = 0
        if sector == 'Single':
            score = points
        elif sector == 'Double':
            score = points * 2
        elif sector == 'Triple':
            score = points * 3

        if score > starting_points:
            unsuccessful_shots += 1
        else:
            starting_points -= score
            successful_shots += 1

        if starting_points == 0:
            print(f'{player_name} won the leg with {successful_shots} shots.')
            break


player = input()
dart_game(player)
