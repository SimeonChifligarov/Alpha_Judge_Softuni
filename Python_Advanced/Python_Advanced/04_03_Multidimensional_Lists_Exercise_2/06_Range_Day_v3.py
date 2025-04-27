from typing import List


def is_valid_position(row: int, col: int, matrix: List[List[str]]) -> bool:
    return 0 <= row < len(matrix) and 0 <= col < len(matrix[row])


if __name__ == '__main__':
    matrix_size = 5
    shooter_symbol, target_symbol, empty_cell = 'A', 'x', '.'
    direction_map = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}
    total_targets, hit_targets, hit_positions = 0, 0, []
    shooter_position, field_matrix = None, []

    for row_index in range(matrix_size):
        current_row = input().split()
        field_matrix.append(current_row)
        if shooter_symbol in current_row:
            shooter_position = (row_index, current_row.index(shooter_symbol))
        total_targets += current_row.count(target_symbol)

    for _ in range(int(input())):
        if hit_targets == total_targets:
            break
        command_parts = input().split()
        action, direction = command_parts[0], command_parts[1]

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

    print(
        f'Training completed! All {hit_targets} targets hit.' if hit_targets == total_targets
        else f'Training not completed! {total_targets - hit_targets} targets left.')
    [print(pos) for pos in hit_positions]
