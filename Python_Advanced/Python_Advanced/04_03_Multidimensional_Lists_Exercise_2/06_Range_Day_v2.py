from typing import List


def is_valid_position(row: int, col: int, matrix: List[List[str]]) -> bool:
    """
    Checks if a given position is inside the matrix.

    Args:
        row: row index
        col: column index
        matrix: the field to check in

    Returns:
        True if position is inside, otherwise False
    """
    return 0 <= row < len(matrix) and 0 <= col < len(matrix[row])


if __name__ == '__main__':
    matrix_size = 5
    shooter_symbol = 'A'
    target_symbol = 'x'
    empty_cell = '.'

    direction_map = {
        'up': (-1, 0),
        'down': (1, 0),
        'left': (0, -1),
        'right': (0, 1),
    }

    total_targets = 0
    hit_targets = 0
    hit_positions = []
    shooter_position = None
    field_matrix = []

    for row_index in range(matrix_size):
        current_row = input().split()
        field_matrix.append(current_row)
        if shooter_symbol in current_row:
            shooter_position = (row_index, current_row.index(shooter_symbol))
        if target_symbol in current_row:
            total_targets += current_row.count(target_symbol)

    command_count = int(input())

    for _ in range(command_count):
        if hit_targets == total_targets:
            break

        command_parts = input().split()
        action = command_parts[0]
        direction = command_parts[1]

        if action == 'move':
            move_steps = int(command_parts[2])
            target_row = shooter_position[0] + direction_map[direction][0] * move_steps
            target_col = shooter_position[1] + direction_map[direction][1] * move_steps

            if not is_valid_position(row=target_row, col=target_col, matrix=field_matrix):
                continue
            if field_matrix[target_row][target_col] != empty_cell:
                continue

            field_matrix[shooter_position[0]][shooter_position[1]] = empty_cell
            shooter_position = (target_row, target_col)
            field_matrix[shooter_position[0]][shooter_position[1]] = shooter_symbol

        elif action == 'shoot':
            for step in range(1, matrix_size + 1):
                shot_row = shooter_position[0] + direction_map[direction][0] * step
                shot_col = shooter_position[1] + direction_map[direction][1] * step

                if not is_valid_position(row=shot_row, col=shot_col, matrix=field_matrix):
                    break

                if field_matrix[shot_row][shot_col] == target_symbol:
                    hit_targets += 1
                    hit_positions.append([shot_row, shot_col])
                    field_matrix[shot_row][shot_col] = empty_cell
                    break

    if hit_targets == total_targets:
        print(f'Training completed! All {hit_targets} targets hit.')
    else:
        print(f'Training not completed! {total_targets - hit_targets} targets left.')

    for pos in hit_positions:
        print(pos)
