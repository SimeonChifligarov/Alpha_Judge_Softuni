def count_attacks(row: int, col: int, board: list[list[str]], size: int) -> int:
    """
    This function counts how many other knights the current knight can attack.

    Args:
    row: row index of the knight
    col: column index of the knight
    board: the chessboard grid
    size: size of the board

    Returns:
    The number of knights that can be attacked from this position
    """
    moves = [
        (-2, -1), (-2, 1),
        (-1, -2), (-1, 2),
        (1, -2), (1, 2),
        (2, -1), (2, 1)
    ]
    attacks = 0

    for dr, dc in moves:
        r, c = row + dr, col + dc
        if 0 <= r < size and 0 <= c < size and board[r][c] == 'K':
            attacks += 1

    return attacks


def remove_knights(board: list[list[str]], size: int) -> int:
    """
    This function removes knights until no more attacks are possible.

    Args:
    board: the chessboard
    size: size of the board

    Returns:
    The number of knights removed
    """
    removed = 0

    while True:
        max_attacks = 0
        knight_to_remove = (-1, -1)

        for row in range(size):
            for col in range(size):
                if board[row][col] == 'K':
                    attacks = count_attacks(row=row, col=col, board=board, size=size)
                    if attacks > max_attacks:
                        max_attacks = attacks
                        knight_to_remove = (row, col)

        if max_attacks == 0:
            break

        r, c = knight_to_remove
        board[r][c] = '0'
        removed += 1

    return removed


if __name__ == '__main__':
    board_size = int(input())
    chess_board = [list(input()) for _ in range(board_size)]

    removed_knights = remove_knights(board=chess_board, size=board_size)
    print(removed_knights)
