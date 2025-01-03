def football_team_statistics(team_name, games_played, results):
    if games_played == 0:
        print(f'{team_name} hasn\'t played any games during this season.')
        return

    points = 0
    wins = 0
    draws = 0
    losses = 0

    for result in results:
        if result == 'W':
            points += 3
            wins += 1
        elif result == 'D':
            points += 1
            draws += 1
        elif result == 'L':
            losses += 1

    win_rate = (wins / games_played) * 100

    print(f'{team_name} has won {points} points during this season.')
    print('Total stats:')
    print(f'## W: {wins}')
    print(f'## D: {draws}')
    print(f'## L: {losses}')
    print(f'Win rate: {win_rate:.2f}%')


team = input()
num_games = int(input())
match_results = [input() for _ in range(num_games)]

football_team_statistics(team_name=team, games_played=num_games, results=match_results)
