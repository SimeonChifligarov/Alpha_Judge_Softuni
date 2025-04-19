def flatten_matrix(matrix_input: list[list[int]]) -> list[int]:
    """
    This function takes a matrix and makes it flat (just one list with all numbers).

    Args:
    matrix_input: a list of lists with the matrix numbers

    Returns:
    A list with all numbers from the matrix, in order
    """
    flat_result = [item for line in matrix_input for item in line]
    return flat_result


if __name__ == '__main__':
    total_rows = int(input())
    matrix_data = []
    for _ in range(total_rows):
        row_elements = input().split(', ')
        row_numbers = [int(part) for part in row_elements]
        matrix_data.append(row_numbers)

    flattened_output = flatten_matrix(matrix_input=matrix_data)
    print(flattened_output)
