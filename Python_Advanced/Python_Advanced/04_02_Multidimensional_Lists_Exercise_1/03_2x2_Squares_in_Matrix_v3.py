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
    return sum(
        1
        for row in range(row_count - 1)
        for col in range(column_count - 1)
        if matrix_data[row][col] == matrix_data[row][col + 1] ==
        matrix_data[row + 1][col] == matrix_data[row + 1][col + 1]
    )


if __name__ == '__main__':
    total_rows, total_columns = [int(x) for x in input().split()]
    matrix = [input().split() for _ in range(total_rows)]

    result = count_equal_2x2_squares(row_count=total_rows, column_count=total_columns, matrix_data=matrix)
    print(result)
