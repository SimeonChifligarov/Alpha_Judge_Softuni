def basketball_tournament():
    total_matches = 0
    total_wins = 0
    total_losses = 0

    while True:
        tournament_name = input()
        if tournament_name == 'End of tournaments':
            break
        matches_count = int(input())
        for match_number in range(1, matches_count + 1):
            desi_points = int(input())
            opponent_points = int(input())
            total_matches += 1
            if desi_points > opponent_points:
                total_wins += 1
                print(f'Game {match_number} of tournament {tournament_name}: win with {desi_points - opponent_points} points.')
            else:
                total_losses += 1
                print(f'Game {match_number} of tournament {tournament_name}: lost with {opponent_points - desi_points} points.')

    win_percentage = (total_wins / total_matches) * 100
    loss_percentage = (total_losses / total_matches) * 100
    print(f'{win_percentage:.2f}% matches win')
    print(f'{loss_percentage:.2f}% matches lost')


if __name__ == '__main__':
    basketball_tournament()
