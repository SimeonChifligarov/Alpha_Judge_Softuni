def calculate_remaining_players(cards: str) -> None:
    """
    Calculates the remaining players on each team based on a sequence of red cards
    and determines if the game was terminated.
    """
    team_a = set(range(1, 12))
    team_b = set(range(1, 12))

    for card in cards.split():
        team, player = card.split('-')
        player = int(player)
        if team == 'A':
            team_a.discard(player)
        elif team == 'B':
            team_b.discard(player)
        if len(team_a) < 7 or len(team_b) < 7:
            print(f'Team A - {len(team_a)}; Team B - {len(team_b)}')
            print('Game was terminated')
            return

    print(f'Team A - {len(team_a)}; Team B - {len(team_b)}')


if __name__ == '__main__':
    cards_input = input()
    calculate_remaining_players(cards=cards_input)
