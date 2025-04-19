def flatten_matrix(matrix_input: list[list[int]]) -> list[int]:
    """
    This function takes a matrix and makes it flat (just one list with all numbers).

    Args:
    rows_input: how many rows the matrix has
    matrix_input: a list of lists with the matrix numbers

    Returns:
    A list with all numbers from the matrix, in order
    """
    flat_result = [item for line in matrix_input for item in line]
    return flat_result


if __name__ == '__main__':
    total_rows = int(input())
    matrix_data = [[int(part) for part in input().split(', ')] for _ in range(total_rows)]

    flattened_output = flatten_matrix(matrix_input=matrix_data)
    print(flattened_output)
