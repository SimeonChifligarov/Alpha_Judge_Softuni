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

    for row in range(row_count - 2):
        for col in range(column_count - 2):
            current_square = [
                [matrix_data[row][col], matrix_data[row][col + 1], matrix_data[row][col + 2]],
                [matrix_data[row + 1][col], matrix_data[row + 1][col + 1], matrix_data[row + 1][col + 2]],
                [matrix_data[row + 2][col], matrix_data[row + 2][col + 1], matrix_data[row + 2][col + 2]]
            ]
            current_sum = sum([value for r in current_square for value in r])

            if current_sum > max_sum:
                max_sum = current_sum
                best_submatrix = current_square

    return max_sum, best_submatrix


if __name__ == '__main__':
    total_rows, total_columns = [int(x) for x in input().split()]
    matrix = [[int(x) for x in input().split()] for _ in range(total_rows)]

    max_total, max_square = find_max_3x3_square(matrix_data=matrix)

    print(f'Sum = {max_total}')
    for line in max_square:
        print(*line)
