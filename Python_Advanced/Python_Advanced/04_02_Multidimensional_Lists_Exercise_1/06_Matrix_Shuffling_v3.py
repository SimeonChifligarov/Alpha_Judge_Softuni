def is_valid_swap(command_parts: list[str], row_count: int, column_count: int) -> bool:
    """
    This function checks if a swap command is correct and all indices are in bounds.

    Args:
    command_parts: the full split command input
    row_count: number of matrix rows
    column_count: number of matrix columns

    Returns:
    True if the command is valid, False otherwise
    """
    if command_parts[0] != 'swap' or len(command_parts) != 5:
        return False

    if not all(el.isdigit() for el in command_parts[1:]):
        return False

    row_1, col_1, row_2, col_2 = int(command_parts[1]), int(command_parts[2]), int(command_parts[3]), int(
        command_parts[4])

    if not (0 <= row_1 < row_count and 0 <= col_1 < column_count and
            0 <= row_2 < row_count and 0 <= col_2 < column_count):
        return False

    return True


def swap_elements(matrix_data: list[list[str]], row_1: int, col_1: int, row_2: int, col_2: int) -> None:
    """
    This function swaps two elements in the matrix.

    Args:
    matrix_data: the matrix to operate on
    row_1: row index of the first element
    col_1: column index of the first element
    row_2: row index of the second element
    col_2: column index of the second element

    Returns:
    Nothing, the matrix is updated in-place
    """
    matrix_data[row_1][col_1], matrix_data[row_2][col_2] = matrix_data[row_2][col_2], matrix_data[row_1][col_1]


if __name__ == '__main__':
    size_parts = input().split()
    total_rows = int(size_parts[0])
    total_columns = int(size_parts[1])

    matrix = []
    for _ in range(total_rows):
        matrix.append(input().split())

    while True:
        command = input()
        if command == 'END':
            break

        parts = command.split()

        if is_valid_swap(command_parts=parts, row_count=total_rows, column_count=total_columns):
            row_a, col_a, row_b, col_b = int(parts[1]), int(parts[2]), int(parts[3]), int(parts[4])

            swap_elements(matrix_data=matrix, row_1=row_a, col_1=col_a, row_2=row_b, col_2=col_b)

            for row in matrix:
                print(' '.join(row))
        else:
            print('Invalid input!')
