def diagonal_difference(matrix_data: list[list[int]]) -> int:
    """
    This function finds the absolute difference between the two diagonals in a square matrix.

    Args:
    matrix_data: a list of lists with matrix numbers

    Returns:
    The absolute difference between the diagonal sums
    """
    return abs(sum(matrix_data[i][i] - matrix_data[i][~i] for i in range(len(matrix_data))))


if __name__ == '__main__':
    size_input = int(input())
    matrix = [[int(x) for x in input().split()] for _ in range(size_input)]

    difference = diagonal_difference(matrix_data=matrix)
    print(difference)
