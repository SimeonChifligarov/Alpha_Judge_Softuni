def count_equal_2x2_squares(row_count: int, column_count: int, matrix_data: list[list[str]]) -> int:
    """
    This function counts how many 2x2 squares in the matrix have the same characters.

    Args:
    row_count: how many rows the matrix has
    column_count: how many columns the matrix has
    matrix_data: the matrix with characters as a list of lists

    Returns:
    The number of 2x2 identical character squares
    """
    square_count = 0

    for row in range(row_count - 1):
        for col in range(column_count - 1):
            current_char = matrix_data[row][col]
            if (
                    matrix_data[row][col + 1] == current_char
                    and matrix_data[row + 1][col] == current_char
                    and matrix_data[row + 1][col + 1] == current_char
            ):
                square_count += 1

    return square_count


if __name__ == '__main__':
    dimensions = input().split()
    total_rows = int(dimensions[0])
    total_columns = int(dimensions[1])

    matrix = []
    for _ in range(total_rows):
        row_data = input().split()
        matrix.append(row_data)

    result = count_equal_2x2_squares(row_count=total_rows, column_count=total_columns, matrix_data=matrix)
    print(result)
