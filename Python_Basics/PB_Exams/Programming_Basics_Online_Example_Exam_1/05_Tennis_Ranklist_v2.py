def calculate_tennis_stats(tournaments_count, starting_points):
    total_points = starting_points
    wins = 0
    points_earned = 0

    for _ in range(tournaments_count):
        stage = input()

        current_points = 0
        if stage == 'W':
            current_points = 2000
            wins += 1
        elif stage == 'F':
            current_points = 1200
        elif stage == 'SF':
            current_points = 720

        points_earned += current_points
        total_points += current_points

    average_points = points_earned // tournaments_count
    win_percentage = (wins / tournaments_count) * 100

    result = [
        f'Final points: {total_points}',
        f'Average points: {average_points}',
        f'{win_percentage:.2f}%',
    ]

    return result


tournaments = int(input())
initial_points = int(input())

res = calculate_tennis_stats(tournaments, initial_points)
print('\n'.join(res))
