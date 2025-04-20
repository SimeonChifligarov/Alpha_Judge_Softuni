def primary_diagonal_sum(matrix_values: list[list[int]]) -> int:
    """
    This function finds the total of the main diagonal in a square matrix.

    Args:
    matrix_size: how many rows and columns the matrix has
    matrix_values: a list of lists with all numbers in the matrix

    Returns:
    The total of the numbers from the top-left to bottom-right diagonal
    """
    return sum(matrix_values[i][i] for i in range(len(matrix_values)))


if __name__ == '__main__':
    size_input = int(input())
    full_matrix = [[int(x) for x in input().split()] for _ in range(size_input)]

    diagonal_total = primary_diagonal_sum(matrix_values=full_matrix)
    print(diagonal_total)
