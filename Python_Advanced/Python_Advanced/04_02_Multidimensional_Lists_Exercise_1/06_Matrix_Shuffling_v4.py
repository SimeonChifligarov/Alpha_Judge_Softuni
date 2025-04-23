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
    try:
        r1, c1, r2, c2 = map(int, command_parts[1:])
        return all(0 <= i < row_count for i in (r1, r2)) and all(0 <= i < column_count for i in (c1, c2))
    except ValueError:
        return False


def swap_elements(matrix_data: list[list[str]], row_1: int, col_1: int, row_2: int, col_2: int) -> None:
    matrix_data[row_1][col_1], matrix_data[row_2][col_2] = matrix_data[row_2][col_2], matrix_data[row_1][col_1]


if __name__ == '__main__':
    total_rows, total_columns = [int(x) for x in input().split()]
    matrix = [input().split() for _ in range(total_rows)]

    while True:
        command = input()
        if command == 'END':
            break

        parts = command.split()

        if is_valid_swap(command_parts=parts, row_count=total_rows, column_count=total_columns):
            r_1, c_1, r_2, c_2 = map(int, parts[1:])
            swap_elements(matrix_data=matrix, row_1=r_1, col_1=c_1, row_2=r_2, col_2=c_2)
            [print(' '.join(row)) for row in matrix]
        else:
            print('Invalid input!')
