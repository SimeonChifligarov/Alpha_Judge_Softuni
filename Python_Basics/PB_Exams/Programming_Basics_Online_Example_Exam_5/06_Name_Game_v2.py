def find_winner():
    winner_name = ''
    winner_score = 0

    while True:
        player_name = input()
        if player_name == 'Stop':
            break

        player_score = 0

        for letter in player_name:
            number = int(input())
            if ord(letter) == number:
                player_score += 10
            else:
                player_score += 2

        if player_score >= winner_score:
            winner_name = player_name
            winner_score = player_score

    print(f'The winner is {winner_name} with {winner_score} points!')


if __name__ == '__main__':
    find_winner()
