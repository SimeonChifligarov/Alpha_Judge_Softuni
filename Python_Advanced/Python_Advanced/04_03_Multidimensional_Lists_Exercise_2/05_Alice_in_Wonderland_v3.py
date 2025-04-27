from typing import List, Tuple, Union


def is_inside_field(row: int, col: int, grid: List[List[Union[int, str]]]) -> bool:
    return 0 <= row < len(grid) and 0 <= col < len(grid[row])


def has_enough_tea(current_tea: int, required_tea: int) -> bool:
    return current_tea >= required_tea


if __name__ == '__main__':
    grid_size = int(input())
    alice_symbol, rabbit_symbol, empty_cell, trail_symbol = 'A', 'R', '.', '*'
    required_bags = 10
    win_message = 'She did it! She went to the party.'
    fail_message = 'Alice didn\'t make it to the tea party.'
    field_matrix, start_position, collected_bags = [], None, 0
    for row_index in range(grid_size):
        row_data = [el if el in [alice_symbol, rabbit_symbol, empty_cell] else int(el) for el in input().split()]
        field_matrix.append(row_data)
        if alice_symbol in row_data:
            start_position = (row_index, row_data.index(alice_symbol))
    direction_map = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}
    current_position = start_position
    while True:
        movement = input()
        field_matrix[current_position[0]][current_position[1]] = trail_symbol
        next_row = current_position[0] + direction_map[movement][0]
        next_col = current_position[1] + direction_map[movement][1]
        if not is_inside_field(row=next_row, col=next_col, grid=field_matrix):
            break
        current_position = (next_row, next_col)
        if field_matrix[current_position[0]][current_position[1]] == rabbit_symbol:
            field_matrix[current_position[0]][current_position[1]] = trail_symbol
            break
        if field_matrix[current_position[0]][current_position[1]] not in [empty_cell, trail_symbol]:
            collected_bags += field_matrix[current_position[0]][current_position[1]]
            if has_enough_tea(current_tea=collected_bags, required_tea=required_bags):
                field_matrix[current_position[0]][current_position[1]] = trail_symbol
                break
    print(win_message if has_enough_tea(current_tea=collected_bags, required_tea=required_bags) else fail_message)
    [print(*row) for row in field_matrix]
