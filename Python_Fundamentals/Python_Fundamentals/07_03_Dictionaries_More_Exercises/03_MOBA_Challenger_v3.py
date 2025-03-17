def process_input() -> dict[str, dict[str, int]]:
    players = {}

    while True:
        data = input()
        if data == 'Season end':
            break

        if ' -> ' in data:
            player, position, skill = data.split(' -> ', maxsplit=2)
            skill = int(skill)

            if player not in players:
                players[player] = {}

            if position not in players[player] or players[player][position] < skill:
                players[player][position] = skill

        elif ' vs ' in data:
            player_1, player_2 = data.split(' vs ', maxsplit=1)

            if player_1 in players and player_2 in players:
                common_positions = set(players[player_1]) & set(players[player_2])

                if common_positions:
                    total_skill_1 = sum(players[player_1].values())
                    total_skill_2 = sum(players[player_2].values())

                    if total_skill_1 > total_skill_2:
                        del players[player_2]
                    elif total_skill_2 > total_skill_1:
                        del players[player_1]

    return players


def print_results(players: dict[str, dict[str, int]]) -> None:
    sorted_players = sorted(players.items(), key=lambda x: (-sum(x[1].values()), x[0]))

    for player, positions in sorted_players:
        total_skill = sum(positions.values())
        print(f'{player}: {total_skill} skill')

        sorted_positions = sorted(positions.items(), key=lambda x: (-x[1], x[0]))
        for position, skill in sorted_positions:
            print(f'- {position} <::> {skill}')


if __name__ == '__main__':
    players_data = process_input()
    print_results(players=players_data)
