def easter_egg_battle(player_one_eggs, player_two_eggs):
    while True:
        command = input()
        if command == 'End':
            print(f'Player one has {player_one_eggs} eggs left.')
            print(f'Player two has {player_two_eggs} eggs left.')
            break

        if command == 'one':
            player_two_eggs -= 1
        elif command == 'two':
            player_one_eggs -= 1

        if player_one_eggs == 0:
            print(f'Player one is out of eggs. Player two has {player_two_eggs} eggs left.')
            break
        if player_two_eggs == 0:
            print(f'Player two is out of eggs. Player one has {player_one_eggs} eggs left.')
            break


player_one_start_eggs = int(input())
player_two_start_eggs = int(input())

easter_egg_battle(player_one_start_eggs, player_two_start_eggs)
