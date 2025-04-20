def find_max_2x2_submatrix(row_count: int, column_count: int, matrix_data: list[list[int]]) -> tuple[
    list[list[int]], int]:
    """
    This function finds the 2x2 square in a matrix that has the biggest sum of numbers.

    Args:
    row_count: how many rows the matrix has
    column_count: how many columns the matrix has
    matrix_data: a list of lists with the matrix numbers

    Returns:
    A tuple with the 2x2 submatrix and the total of its numbers
    """

    max_sum, best_square = max(
        (
            (sum([matrix_data[r][c], matrix_data[r][c + 1], matrix_data[r + 1][c], matrix_data[r + 1][c + 1]]),
             [[matrix_data[r][c], matrix_data[r][c + 1]], [matrix_data[r + 1][c], matrix_data[r + 1][c + 1]]])
            for r in range(row_count - 1) for c in range(column_count - 1)
        ),
        key=lambda x: x[0]
    )

    return best_square, max_sum


if __name__ == '__main__':
    total_rows, total_columns = [int(x) for x in input().split(', ')]
    full_matrix = [[int(x) for x in input().split(', ')] for _ in range(total_rows)]

    best_submatrix, submatrix_sum = find_max_2x2_submatrix(
        row_count=total_rows,
        column_count=total_columns,
        matrix_data=full_matrix
    )

    for line in best_submatrix:
        print(*line)
    print(submatrix_sum)
