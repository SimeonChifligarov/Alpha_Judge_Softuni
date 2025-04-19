def get_matrix_sum_and_display(rows: int, columns: int, data: list[list[int]]) -> tuple[int, list[list[int]]]:
    """
    This function calculates the sum of all numbers in a matrix.

    Args:
    rows: number of rows in the matrix
    columns: number of columns in the matrix
    data: list of lists, where each inner list is a row of integers

    Returns:
    The sum of all numbers and the matrix itself
    """
    total_sum = sum([element for row in data for element in row])
    return total_sum, data


if __name__ == '__main__':
    dimensions = [int(x) for x in input().split(', ')]
    rows_count, columns_count = dimensions[0], dimensions[1]
    matrix_data = [[int(x) for x in input().split(', ')] for _ in range(rows_count)]

    result_sum, result_matrix = get_matrix_sum_and_display(rows=rows_count, columns=columns_count, data=matrix_data)
    print(result_sum)
    print(result_matrix)
