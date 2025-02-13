from typing import List


def check_tic_tac_toe_winner(field: List[List[int]]) -> str:
    """
    Determines the winner of a Tic-Tac-Toe game given the field.
    Returns:
    - "First player won" if the first player wins
    - "Second player won" if the second player wins
    - "Draw!" if there is no winner
    """

    for i in range(3):
        # Check rows and columns
        if field[i][0] == field[i][1] == field[i][2] != 0:
            return 'First player won' if field[i][0] == 1 else 'Second player won'
        if field[0][i] == field[1][i] == field[2][i] != 0:
            return 'First player won' if field[0][i] == 1 else 'Second player won'

    # Check diagonals
    if field[0][0] == field[1][1] == field[2][2] != 0:
        return 'First player won' if field[0][0] == 1 else 'Second player won'
    if field[0][2] == field[1][1] == field[2][0] != 0:
        return 'First player won' if field[0][2] == 1 else 'Second player won'

    return 'Draw!'


if __name__ == '__main__':
    # field_input = [list(map(int, input().split())) for _ in range(3)]
    field_input = [[int(x) for x in input().split()] for _ in range(3)]
    result = check_tic_tac_toe_winner(field=field_input)
    print(result)
