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
    direction_moves = {
        'up': (-1, 0),
        'down': (1, 0),
        'left': (0, -1),
        'right': (0, 1),
    }

    path = []
    eggs = 0
    delta_row, delta_col = direction_moves[direction]
    row = start_row + delta_row
    col = start_col + delta_col

    while 0 <= row < size and 0 <= col < size:
        if matrix[row][col] == 'X':
            break
        eggs += int(matrix[row][col])
        path.append([row, col])
        row += delta_row
        col += delta_col

    return path, eggs


def find_best_path(matrix: list[list[str]], size: int) -> tuple[str, list[list[int]], int]:
    """
    This function finds the best direction for the bunny to collect maximum eggs.

    Args:
    matrix: the field matrix
    size: the size of the matrix

    Returns:
    A tuple with best direction, the path taken (as lists), and the total eggs collected
    """
    for row in range(size):
        for col in range(size):
            if matrix[row][col] == 'B':
                bunny_row, bunny_col = row, col

    best_direction = ''
    best_path = []
    max_eggs = -1  # Handles case where all directions give 0 eggs

    for direction in ['up', 'down', 'left', 'right']:
        path, eggs = collect_eggs(matrix=matrix, start_row=bunny_row, start_col=bunny_col, direction=direction,
                                  size=size)
        if eggs > max_eggs:
            max_eggs = eggs
            best_path = path
            best_direction = direction

    return best_direction, best_path, max_eggs


if __name__ == '__main__':
    field_size = int(input())
    field = [input().split() for _ in range(field_size)]

    best_dir, best_positions, total_eggs = find_best_path(matrix=field, size=field_size)

    print(best_dir)
    for pos in best_positions:
        print(pos)
    print(total_eggs)
