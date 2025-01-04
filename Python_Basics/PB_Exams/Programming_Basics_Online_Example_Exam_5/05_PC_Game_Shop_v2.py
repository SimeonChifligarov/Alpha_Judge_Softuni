games_count = {
    'Hearthstone': 0,
    'Fornite': 0,
    'Overwatch': 0,
    'Others': 0,  # this will fail if game name is 'Others'
}

games_sold = int(input())
for _ in range(games_sold):
    game = input()
    if game in games_count:
        games_count[game] += 1
    else:
        games_count['Others'] += 1

for game_name, game_count in games_count.items():
    print(f'{game_name} - {(game_count / games_sold):.2%}')
