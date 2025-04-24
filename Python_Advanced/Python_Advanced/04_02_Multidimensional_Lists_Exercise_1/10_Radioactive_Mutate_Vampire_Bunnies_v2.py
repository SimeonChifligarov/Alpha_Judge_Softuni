def spread_bunnies(lair: list[list[str]], rows: int, cols: int) -> list[list[str]]:
    """
    This function spreads the bunnies one step in all four directions.

    Args:
    lair: the current lair grid
    rows: number of rows
    cols: number of columns

    Returns:
    A new lair grid after bunny spread
    """
    new_lair = [row[:] for row in lair]

    for row in range(rows):
        for col in range(cols):
            if lair[row][col] == 'B':
                for r, c in [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]:
                    if 0 <= r < rows and 0 <= c < cols:
                        new_lair[r][c] = 'B'

    return new_lair


def play_game(rows: int, cols: int, lair: list[list[str]], moves: str) -> tuple[list[list[str]], str]:
    """
    This function plays the full game turn by turn, checking win or death.

    Args:
    rows: number of rows in the lair
    cols: number of columns in the lair
    lair: the initial lair grid
    moves: string with movement directions

    Returns:
    A tuple: final lair grid and result message ("won"/"dead" with coordinates)
    """
    directions = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}

    for row in range(rows):
        for col in range(cols):
            if lair[row][col] == 'P':
                player_row, player_col = row, col

    for move in moves:
        d_row, d_col = directions[move]
        next_row = player_row + d_row
        next_col = player_col + d_col

        lair[player_row][player_col] = '.'

        if not (0 <= next_row < rows and 0 <= next_col < cols):
            lair = spread_bunnies(lair=lair, rows=rows, cols=cols)
            return lair, f'won: {player_row} {player_col}'

        if lair[next_row][next_col] == 'B':
            lair = spread_bunnies(lair=lair, rows=rows, cols=cols)
            return lair, f'dead: {next_row} {next_col}'

        lair[next_row][next_col] = 'P'
        player_row, player_col = next_row, next_col
        lair = spread_bunnies(lair=lair, rows=rows, cols=cols)

        if lair[player_row][player_col] == 'B':
            return lair, f'dead: {player_row} {player_col}'

    return lair, f'dead: {player_row} {player_col}'


if __name__ == '__main__':
    size_input = input().split()
    total_rows = int(size_input[0])
    total_cols = int(size_input[1])

    lair_matrix = []
    for _ in range(total_rows):
        lair_matrix.append(list(input()))

    move_sequence = input()

    final_lair, outcome = play_game(rows=total_rows, cols=total_cols, lair=lair_matrix, moves=move_sequence)

    for row in final_lair:
        print(''.join(row))
    print(outcome)
