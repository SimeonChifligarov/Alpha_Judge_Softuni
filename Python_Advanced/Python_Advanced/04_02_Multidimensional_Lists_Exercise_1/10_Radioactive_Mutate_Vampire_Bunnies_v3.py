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
    return [['B' if lair[r][c] == 'B' or any(
        0 <= nr < rows and 0 <= nc < cols and lair[nr][nc] == 'B'
        for nr, nc in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]
    ) else lair[r][c] for c in range(cols)] for r in range(rows)]


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
    pr, pc = [(r, c) for r in range(rows) for c in range(cols) if lair[r][c] == 'P'][0]

    for move in moves:
        dr, dc = directions[move]
        nr, nc = pr + dr, pc + dc
        lair[pr][pc] = '.'

        if not (0 <= nr < rows and 0 <= nc < cols):
            lair = spread_bunnies(lair, rows, cols)
            return lair, f'won: {pr} {pc}'

        if lair[nr][nc] == 'B':
            lair = spread_bunnies(lair, rows, cols)
            return lair, f'dead: {nr} {nc}'

        lair[nr][nc] = 'P'
        pr, pc = nr, nc
        lair = spread_bunnies(lair, rows, cols)

        if lair[pr][pc] == 'B':
            return lair, f'dead: {pr} {pc}'

    return lair, f'dead: {pr} {pc}'


if __name__ == '__main__':
    total_rows, total_cols = [int(x) for x in input().split()]
    lair_matrix = [list(input()) for _ in range(total_rows)]
    move_sequence = input()

    final_lair, outcome = play_game(rows=total_rows, cols=total_cols, lair=lair_matrix, moves=move_sequence)

    [print(''.join(row)) for row in final_lair]
    print(outcome)
