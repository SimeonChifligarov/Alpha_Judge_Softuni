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
    max_sum = float('-inf')
    best_square = []

    for row in range(row_count - 1):
        for col in range(column_count - 1):
            current_square = [
                [matrix_data[row][col], matrix_data[row][col + 1]],
                [matrix_data[row + 1][col], matrix_data[row + 1][col + 1]]
            ]
            current_sum = sum([value for sub_row in current_square for value in sub_row])

            if current_sum > max_sum:
                max_sum = current_sum
                best_square = current_square

    return best_square, max_sum


if __name__ == '__main__':
    size_input = input().split(', ')
    total_rows = int(size_input[0])
    total_columns = int(size_input[1])

    full_matrix = []
    for _ in range(total_rows):
        row_data = [int(x) for x in input().split(', ')]
        full_matrix.append(row_data)

    best_submatrix, submatrix_sum = find_max_2x2_submatrix(
        row_count=total_rows,
        column_count=total_columns,
        matrix_data=full_matrix
    )

    for line in best_submatrix:
        print(*line)
    print(submatrix_sum)
