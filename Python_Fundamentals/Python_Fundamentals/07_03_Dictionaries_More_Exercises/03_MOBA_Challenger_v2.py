def process_season():
    player_data = {}

    while True:
        command = input()
        if command == 'Season end':
            break

        if ' -> ' in command:
            player, position, skill = command.split(' -> ', maxsplit=2)
            skill = int(skill)

            if player not in player_data:
                player_data[player] = {}

            if position not in player_data[player] or player_data[player][position] < skill:
                player_data[player][position] = skill

        elif ' vs ' in command:
            player1, player2 = command.split(' vs ')

            if player1 in player_data and player2 in player_data:
                common_positions = set(player_data[player1]) & set(player_data[player2])

                if common_positions:
                    total_skill1 = sum(player_data[player1].values())
                    total_skill2 = sum(player_data[player2].values())

                    if total_skill1 > total_skill2:
                        del player_data[player2]
                    elif total_skill1 < total_skill2:
                        del player_data[player1]

    sorted_players = sorted(player_data.items(), key=lambda x: (-sum(x[1].values()), x[0]))

    for player, positions in sorted_players:
        total_skill = sum(positions.values())
        print(f'{player}: {total_skill} skill')
        for position, skill in sorted(positions.items(), key=lambda x: (-x[1], x[0])):
            print(f'- {position} <::> {skill}')


if __name__ == '__main__':
    process_season()
