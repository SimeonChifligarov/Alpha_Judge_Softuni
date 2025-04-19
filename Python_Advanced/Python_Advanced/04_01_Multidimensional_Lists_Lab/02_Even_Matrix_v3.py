def extract_even_matrix(matrix_values: list[list[int]]) -> list[list[int]]:
    """
    This function creates a new matrix with only the even numbers.

    Args:
    row_total: how many rows are in the matrix
    matrix_values: a list of lists with all numbers from the matrix

    Returns:
    A new matrix that keeps only the even numbers
    """
    even_matrix = [[value for value in row if value % 2 == 0] for row in matrix_values]
    return even_matrix


if __name__ == '__main__':
    row_count = int(input())
    original_matrix = [[int(x) for x in input().split(', ')] for _ in range(row_count)]

    filtered_matrix = extract_even_matrix(matrix_values=original_matrix)
    print(filtered_matrix)
