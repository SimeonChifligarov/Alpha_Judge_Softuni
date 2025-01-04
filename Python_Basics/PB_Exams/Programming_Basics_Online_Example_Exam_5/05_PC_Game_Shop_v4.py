def calculate_game_sales_percentage(total_sales, games_list):
    game_counts = {'Hearthstone': 0, 'Fornite': 0, 'Overwatch': 0, 'Others': 0}

    for game in games_list:
        if game in game_counts:
            game_counts[game] += 1
        else:
            game_counts['Others'] += 1

    for game, count in game_counts.items():
        percentage = (count / total_sales) * 100
        print(f'{game} - {percentage:.2f}%')


n_sales = int(input())
games = [input() for _ in range(n_sales)]
calculate_game_sales_percentage(total_sales=n_sales, games_list=games)
