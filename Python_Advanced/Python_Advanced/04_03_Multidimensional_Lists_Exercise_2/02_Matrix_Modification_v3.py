def are_coordinates_valid(matrix_data: list[list[int]], row_index: int, col_index: int) -> bool:
    """
    This function checks if given coordinates are inside the matrix bounds.

    Args:
    matrix_data: the matrix to check against
    row_index: the row index to check
    col_index: the column index to check

    Returns:
    True if the coordinates are valid, False otherwise
    """
    return 0 <= row_index < len(matrix_data) and 0 <= col_index < len(matrix_data[0])


def modify_matrix(matrix_data: list[list[int]], command_parts: list[str]) -> None:
    """
    This function modifies the matrix based on the command provided.

    Args:
    matrix_data: the current matrix to modify
    command_parts: a list with command type, row, col, and value

    Returns:
    Nothing; matrix is updated in place
    """
    action = command_parts[0]
    row_index = int(command_parts[1])
    col_index = int(command_parts[2])
    value = int(command_parts[3])

    if are_coordinates_valid(matrix_data=matrix_data, row_index=row_index, col_index=col_index):
        if action == 'Add':
            matrix_data[row_index][col_index] += value
        elif action == 'Subtract':
            matrix_data[row_index][col_index] -= value
    else:
        print('Invalid coordinates')


if __name__ == '__main__':
    row_count = int(input())

    matrix = []
    for _ in range(row_count):
        row_data = [int(x) for x in input().split()]
        matrix.append(row_data)

    while True:
        command = input()
        if command == 'END':
            break

        parts = command.split()
        modify_matrix(matrix_data=matrix, command_parts=parts)

    for row in matrix:
        print(*row)
