def collect_eggs(matrix: list[list[str]], start_row: int, start_col: int, direction: str, size: int) -> tuple[
    list[list[int]], int]:
    """
    This function simulates collecting eggs in a direction until a trap or boundary.

    Args:
    matrix: the field matrix
    start_row: starting row position
    start_col: starting column position
    direction: direction to move in ('up', 'down', 'left', 'right')
    size: the size of the square matrix

    Returns:
    A tuple with a list of coordinates visited (as lists) and the total eggs collected
    """
    deltas = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}
    path, eggs = [], 0
    dr, dc = deltas[direction]
    r, c = start_row + dr, start_col + dc

    while 0 <= r < size and 0 <= c < size and matrix[r][c] != 'X':
        eggs += int(matrix[r][c])
        path.append([r, c])
        r += dr
        c += dc

    return path, eggs


def find_best_path(matrix: list[list[str]], size: int) -> tuple[str, list[list[int]], int]:
    br, bc = next((r, c) for r in range(size) for c in range(size) if matrix[r][c] == 'B')
    best = max(
        (collect_eggs(matrix, br, bc, d, size) + (d,) for d in ['up', 'down', 'left', 'right']),
        key=lambda x: x[1]
    )
    return best[2], best[0], best[1]


if __name__ == '__main__':
    size = int(input())
    field = [input().split() for _ in range(size)]
    direction, path, total = find_best_path(matrix=field, size=size)
    print(direction)
    for pos in path:
        print(pos)
    print(total)
