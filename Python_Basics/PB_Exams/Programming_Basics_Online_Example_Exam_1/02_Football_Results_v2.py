def analyze_matches(results):
    wins = 0
    losses = 0
    draws = 0

    for result in results:
        home_goals, away_goals = map(int, result.split(':'))
        if home_goals > away_goals:
            wins += 1
        elif home_goals < away_goals:
            losses += 1
        else:
            draws += 1

    return wins, losses, draws


def main():
    res = [input() for _ in range(3)]
    wins, losses, draws = analyze_matches(res)
    print(f'Team won {wins} games.')
    print(f'Team lost {losses} games.')
    print(f' Drawn games: {draws}')


if __name__ == '__main__':
    main()
