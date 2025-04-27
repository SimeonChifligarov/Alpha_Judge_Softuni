def is_valid_position(row: int, col: int) -> bool:
    """
    This function checks if a position is within the 5x5 field.

    Args:
    row: row index
    col: column index

    Returns:
    True if the position is valid, otherwise False
    """
    return 0 <= row < 5 and 0 <= col < 5


def move_player(position: tuple[int, int], direction: str, steps: int, field: list[list[str]]) -> tuple[int, int]:
    """
    This function attempts to move the player a number of steps in a direction.

    Args:
    position: current position (row, col)
    direction: direction to move in
    steps: number of steps to move
    field: the game matrix

    Returns:
    New position if move is possible, else original position
    """
    direction_map = {
        'up': (-1, 0),
        'down': (1, 0),
        'left': (0, -1),
        'right': (0, 1)
    }

    delta_row, delta_col = direction_map[direction]
    row, col = position

    for _ in range(steps):
        next_row = row + delta_row
        next_col = col + delta_col
        if is_valid_position(next_row, next_col) and field[next_row][next_col] == '.':
            row, col = next_row, next_col
        else:
            break

    return row, col


def shoot(direction: str, position: tuple[int, int], field: list[list[str]]) -> tuple[bool, list[int]]:
    """
    This function simulates a shot in the given direction.

    Args:
    direction: the shooting direction
    position: current shooter position
    field: the game matrix

    Returns:
    A tuple: whether a target was hit, and the hit target's coordinates
    """
    direction_map = {
        'up': (-1, 0),
        'down': (1, 0),
        'left': (0, -1),
        'right': (0, 1),
    }

    delta_row, delta_col = direction_map[direction]
    row, col = position

    while is_valid_position(row + delta_row, col + delta_col):
        row += delta_row
        col += delta_col
        if field[row][col] == 'x':
            field[row][col] = '.'
            return True, [row, col]

    return False, []


if __name__ == '__main__':
    field = []
    player_position = (0, 0)
    total_targets = 0

    for r in range(5):
        row_data = input().split()
        field.append(row_data)
        if 'A' in row_data:
            player_position = (r, row_data.index('A'))
        total_targets += row_data.count('x')

    field[player_position[0]][player_position[1]] = '.'

    hit_targets = []

    command_count = int(input())
    for _ in range(command_count):
        parts = input().split()
        action = parts[0]
        direction = parts[1]

        if action == 'move':
            steps = int(parts[2])
            player_position = move_player(position=player_position, direction=direction, steps=steps, field=field)
        elif action == 'shoot':
            hit, coords = shoot(direction=direction, position=player_position, field=field)
            if hit:
                hit_targets.append(coords)
                if len(hit_targets) == total_targets:
                    break

    if len(hit_targets) == total_targets:
        print(f'Training completed! All {total_targets} targets hit.')
    else:
        print(f'Training not completed! {total_targets - len(hit_targets)} targets left.')

    for target in hit_targets:
        print(target)
