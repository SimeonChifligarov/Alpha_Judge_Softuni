from typing import List


def is_within_bounds(row_index: int, col_index: int, matrix: List[List[str]]) -> bool:
    return 0 <= row_index < len(matrix) and 0 <= col_index < len(matrix[row_index])


if __name__ == '__main__':
    total_presents = int(input())
    field_size = int(input())
    santa_char, naughty_kid_char, nice_kid_char, cookie_char, empty_char = 'S', 'X', 'V', 'C', '-'
    stop_command = 'Christmas morning'
    direction_map = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}
    santa_coords, total_nice_kids, happy_nice_kids, field_grid = None, 0, 0, []

    for row_num in range(field_size):
        line = input().split()
        field_grid.append(line)
        if santa_char in line:
            santa_coords = (row_num, line.index(santa_char))
        total_nice_kids += line.count(nice_kid_char)

    while total_presents > 0:
        current_command = input()
        if current_command == stop_command:
            break
        next_row = santa_coords[0] + direction_map[current_command][0]
        next_col = santa_coords[1] + direction_map[current_command][1]
        if not is_within_bounds(row_index=next_row, col_index=next_col, matrix=field_grid):
            break
        field_grid[santa_coords[0]][santa_coords[1]] = empty_char
        santa_coords = (next_row, next_col)
        current_symbol = field_grid[santa_coords[0]][santa_coords[1]]
        if current_symbol == nice_kid_char:
            total_presents -= 1
            happy_nice_kids += 1
        elif current_symbol == cookie_char:
            for move in direction_map.values():
                adj_row = santa_coords[0] + move[0]
                adj_col = santa_coords[1] + move[1]
                if not is_within_bounds(row_index=adj_row, col_index=adj_col, matrix=field_grid):
                    continue
                adjacent_symbol = field_grid[adj_row][adj_col]
                if adjacent_symbol in [nice_kid_char, naughty_kid_char]:
                    total_presents -= 1
                    if adjacent_symbol == nice_kid_char:
                        happy_nice_kids += 1
                    field_grid[adj_row][adj_col] = empty_char
                    if total_presents == 0:
                        break
        field_grid[santa_coords[0]][santa_coords[1]] = santa_char

    if total_presents == 0 and happy_nice_kids < total_nice_kids:
        print('Santa ran out of presents!')
    [print(*row) for row in field_grid]
    print(
        f'Good job, Santa! {happy_nice_kids} happy nice kid/s.' if happy_nice_kids == total_nice_kids
        else f'No presents for {total_nice_kids - happy_nice_kids} nice kid/s.')
