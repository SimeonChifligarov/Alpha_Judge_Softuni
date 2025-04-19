def sum_columns(row_count: int, column_count: int, matrix_data: list[list[int]]) -> list[int]:
    """
    This function adds the numbers in each column of a matrix.

    Args:
    row_count: how many rows the matrix has
    column_count: how many columns the matrix has
    matrix_data: a list of lists with all numbers from the matrix

    Returns:
    A list where each number is the total of a column
    """
    column_sums = [sum(matrix_data[row][col] for row in range(row_count)) for col in range(column_count)]
    return column_sums


if __name__ == '__main__':
    size_values = [int(x) for x in input().split(', ')]
    row_total, column_total = size_values[0], size_values[1]

    matrix_input = []
    for _ in range(row_total):
        current_row = [int(x) for x in input().split()]
        matrix_input.append(current_row)

    column_totals = sum_columns(row_count=row_total, column_count=column_total, matrix_data=matrix_input)
    for total in column_totals:
        print(total)
