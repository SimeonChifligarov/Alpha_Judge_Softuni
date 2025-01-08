def christmas_tournament(days, results):
    total_money = 0
    winning_days = 0

    for day in range(days):
        day_wins = 0
        day_losses = 0
        day_money = 0

        for game, outcome in results[day]:
            if outcome == 'win':
                day_wins += 1
                day_money += 20
            elif outcome == 'lose':
                day_losses += 1

        if day_wins > day_losses:
            day_money *= 1.10
            winning_days += 1

        total_money += day_money

    if winning_days > days / 2:
        total_money *= 1.20
        return f'You won the tournament! Total raised money: {total_money:.2f}'
    else:
        return f'You lost the tournament! Total raised money: {total_money:.2f}'


if __name__ == '__main__':
    tournament_days = int(input())
    tournament_results = []

    for _ in range(tournament_days):
        daily_results = []
        while True:
            sport = input()
            if sport == 'Finish':
                break
            res = input()
            daily_results.append((sport, res))
        tournament_results.append(daily_results)

    result = christmas_tournament(days=tournament_days, results=tournament_results)
    print(result)
