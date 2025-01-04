def calculate_game_sales_percentage(total_sales, games_list):
    hearthstone_count = 0
    fortnite_count = 0
    overwatch_count = 0
    other_count = 0

    for game in games_list:
        if game == 'Hearthstone':
            hearthstone_count += 1
        elif game == 'Fornite':
            fortnite_count += 1
        elif game == 'Overwatch':
            overwatch_count += 1
        else:
            other_count += 1

    hearthstone_percentage = (hearthstone_count / total_sales) * 100
    fortnite_percentage = (fortnite_count / total_sales) * 100
    overwatch_percentage = (overwatch_count / total_sales) * 100
    others_percentage = (other_count / total_sales) * 100

    print(f'Hearthstone - {hearthstone_percentage:.2f}%')
    print(f'Fornite - {fortnite_percentage:.2f}%')
    print(f'Overwatch - {overwatch_percentage:.2f}%')
    print(f'Others - {others_percentage:.2f}%')


n_sales = int(input())
games = [input() for _ in range(n_sales)]
calculate_game_sales_percentage(total_sales=n_sales, games_list=games)
