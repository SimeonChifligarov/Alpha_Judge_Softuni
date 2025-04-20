def primary_diagonal_sum(matrix_size: int, matrix_values: list[list[int]]) -> int:
    """
    This function finds the total of the main diagonal in a square matrix.

    Args:
    matrix_size: how many rows and columns the matrix has
    matrix_values: a list of lists with all numbers in the matrix

    Returns:
    The total of the numbers from the top-left to bottom-right diagonal
    """
    total = 0
    for index in range(matrix_size):
        total += matrix_values[index][index]
    return total


if __name__ == '__main__':
    size_input = int(input())

    full_matrix = []
    for _ in range(size_input):
        row_data = [int(x) for x in input().split()]
        full_matrix.append(row_data)

    diagonal_total = primary_diagonal_sum(matrix_size=size_input, matrix_values=full_matrix)
    print(diagonal_total)
