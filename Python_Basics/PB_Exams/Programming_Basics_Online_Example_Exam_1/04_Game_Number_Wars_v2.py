def play_numbers_game(player_one_name, player_two_name):
    player_one_points = 0
    player_two_points = 0

    while True:
        command = input()
        if command == 'End of game':
            print(f'{player_one_name} has {player_one_points} points')
            print(f'{player_two_name} has {player_two_points} points')
            break

        player_one_card = int(command)
        player_two_card = int(input())

        if player_one_card == player_two_card:
            print('Number wars!')
            player_one_card = int(input())
            player_two_card = int(input())

            if player_one_card > player_two_card:
                print(f'{player_one_name} is winner with {player_one_points} points')
            else:
                print(f'{player_two_name} is winner with {player_two_points} points')
            break

        elif player_one_card > player_two_card:
            player_one_points += player_one_card - player_two_card
        else:
            player_two_points += player_two_card - player_one_card


name_one = input()
name_two = input()

play_numbers_game(name_one, name_two)
