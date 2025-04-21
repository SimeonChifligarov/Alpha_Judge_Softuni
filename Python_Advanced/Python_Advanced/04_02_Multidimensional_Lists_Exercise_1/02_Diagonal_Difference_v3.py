def diagonal_difference(matrix_size: int, matrix_data: list[list[int]]) -> int:
    """
    This function finds the absolute difference between the two diagonals in a square matrix.

    Args:
    matrix_size: how many rows and columns the matrix has
    matrix_data: a list of lists with matrix numbers

    Returns:
    The absolute difference between the diagonal sums
    """
    primary_sum = sum(matrix_data[i][i] for i in range(matrix_size))
    secondary_sum = sum(matrix_data[i][matrix_size - i - 1] for i in range(matrix_size))
    return abs(primary_sum - secondary_sum)


if __name__ == '__main__':
    size_input = int(input())
    matrix = [[int(x) for x in input().split()] for _ in range(size_input)]

    difference = diagonal_difference(matrix_size=size_input, matrix_data=matrix)
    print(difference)
