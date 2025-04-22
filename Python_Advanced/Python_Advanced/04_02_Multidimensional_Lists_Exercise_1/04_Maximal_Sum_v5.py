def find_max_3x3_square(matrix_data: list[list[int]]) -> tuple[int, list[list[int]]]:
    """
    This function finds the 3x3 square in the matrix with the highest sum.

    Args:
    matrix_data: a list of lists with all the matrix numbers

    Returns:
    The highest sum and the corresponding 3x3 submatrix
    """
    row_count = len(matrix_data)
    column_count = len(matrix_data[0])
    max_sum = float('-inf')
    best_submatrix = []

    max_sum, best_submatrix = max(
        (
            (sum(matrix_data[r + i][c + j] for i in range(3) for j in range(3)),
             [[matrix_data[r + i][c + j] for j in range(3)] for i in range(3)])
            for r in range(row_count - 2) for c in range(column_count - 2)
        ),
        key=lambda x: x[0]
    )
    return max_sum, best_submatrix


if __name__ == '__main__':
    total_rows, total_columns = [int(x) for x in input().split()]
    matrix = [[int(x) for x in input().split()] for _ in range(total_rows)]

    max_total, max_square = find_max_3x3_square(matrix_data=matrix)

    print(f'Sum = {max_total}')
    for line in max_square:
        print(*line)
