def count_equal_2x2_squares(matrix_data: list[list[str]]) -> int:
    """
    This function counts how many 2x2 squares in the matrix have the same characters.

    Args:
    matrix_data: the matrix with characters as a list of lists

    Returns:
    The number of 2x2 identical character squares
    """
    row_count = len(matrix_data)
    column_count = len(matrix_data[0])
    return sum(matrix_data[r][c] == matrix_data[r][c + 1] == matrix_data[r + 1][c] == matrix_data[r + 1][c + 1] for r in
               range(row_count - 1) for c in range(column_count - 1))


if __name__ == '__main__':
    total_rows, total_columns = [int(x) for x in input().split()]
    matrix = [input().split() for _ in range(total_rows)]

    result = count_equal_2x2_squares(matrix_data=matrix)
    print(result)
