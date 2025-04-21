def get_diagonals(matrix_size: int, matrix_data: list[list[int]]) -> tuple[list[int], list[int]]:
    """
    This function gets both diagonals from a square matrix.

    Args:
    matrix_size: how many rows and columns the matrix has
    matrix_data: a list of lists with matrix numbers

    Returns:
    A tuple with two lists: the primary and secondary diagonals
    """
    primary = [matrix_data[i][i] for i in range(matrix_size)]
    secondary = [matrix_data[i][matrix_size - i - 1] for i in range(matrix_size)]
    return primary, secondary


if __name__ == '__main__':
    matrix_size_input = int(input())
    matrix = [[int(x) for x in input().split(', ')] for _ in range(matrix_size_input)]

    primary_diagonal, secondary_diagonal = get_diagonals(
        matrix_size=matrix_size_input,
        matrix_data=matrix
    )

    print(f'Primary diagonal: {", ".join([str(el) for el in primary_diagonal])}. Sum: {sum(primary_diagonal)}')
    print(f'Secondary diagonal: {", ".join([str(el) for el in secondary_diagonal])}. Sum: {sum(secondary_diagonal)}')
