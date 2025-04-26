from typing import List, Tuple, Union


def check_coords_valid(row_index: int, col_index: int, grid: List[List[Union[int, str]]]) -> bool:
    """
    Checks if the coordinates are inside the grid.

    Args:
        row_index: the row index
        col_index: the column index
        grid: the field matrix

    Returns:
        True if the position is valid, otherwise False
    """
    return 0 <= row_index < len(grid) and 0 <= col_index < len(grid[row_index])


def find_best_path(field_matrix: List[List[Union[int, str]]], bunny_coords: Tuple[int, int]) -> List[
    Union[str, List[int], int]]:
    """
    Finds the best path for the bunny to collect the most eggs.

    Args:
        field_matrix: the whole grid of the field
        bunny_coords: the starting position of the bunny

    Returns:
        A list with the best direction, path taken, and total eggs collected
    """
    directions_map = {
        'up': (-1, 0),
        'down': (1, 0),
        'left': (0, -1),
        'right': (0, 1),
    }

    trap_symbol = 'X'
    max_eggs = 0
    best_direction = None
    best_path = []

    for direction, movement in directions_map.items():
        collected_eggs = 0
        path_taken = []
        row, col = bunny_coords[0] + movement[0], bunny_coords[1] + movement[1]

        while check_coords_valid(row_index=row, col_index=col, grid=field_matrix):
            if field_matrix[row][col] == trap_symbol:
                break

            collected_eggs += field_matrix[row][col]
            path_taken.append([row, col])
            row += movement[0]
            col += movement[1]

        if collected_eggs >= max_eggs:
            max_eggs = collected_eggs
            best_direction = direction
            best_path = path_taken

    return [best_direction] + best_path + [max_eggs]


if __name__ == '__main__':
    field_size = int(input())
    bunny_symbol = 'B'

    matrix = []
    bunny_position = None

    for row_idx in range(field_size):
        current_row = [el if el in ['B', 'X'] else int(el) for el in input().split()]
        matrix.append(current_row)
        if bunny_symbol in current_row:
            bunny_position = (row_idx, current_row.index(bunny_symbol))

    final_result = find_best_path(field_matrix=matrix, bunny_coords=bunny_position)

    for element in final_result:
        print(element)
