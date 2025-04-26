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
    directions = [(-2, -1), (-2, 1), (-1, -2), (-1, 2),
                  (1, -2), (1, 2), (2, -1), (2, 1)]
    return sum(1 for dr, dc in directions
               if 0 <= row + dr < size and 0 <= col + dc < size and board[row + dr][col + dc] == 'K')


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
        target = None
        for r in range(size):
            for c in range(size):
                if board[r][c] == 'K':
                    attacks = count_attacks(r, c, board, size)
                    if attacks > max_attacks:
                        max_attacks = attacks
                        target = (r, c)
        if not target:
            break
        board[target[0]][target[1]] = '0'
        removed += 1
    return removed


if __name__ == '__main__':
    size = int(input())
    board = [list(input()) for _ in range(size)]
    print(remove_knights(board=board, size=size))
