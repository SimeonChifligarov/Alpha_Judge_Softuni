def extract_diagonals(matrix_size: int, matrix_data: list[list[int]]) -> tuple[list[int], list[int]]:
    """
    This function gets the primary and secondary diagonals from a square matrix.

    Args:
    matrix_size: how many rows and columns the matrix has
    matrix_data: a list of lists with the matrix numbers

    Returns:
    Two lists: the primary diagonal and the secondary diagonal
    """
    main_diagonal = []
    other_diagonal = []

    for index in range(matrix_size):
        main_diagonal.append(matrix_data[index][index])
        other_diagonal.append(matrix_data[index][matrix_size - index - 1])

    return main_diagonal, other_diagonal


if __name__ == '__main__':
    size_input = int(input())

    full_matrix = []
    for _ in range(size_input):
        row_data = [int(x) for x in input().split(', ')]
        full_matrix.append(row_data)

    primary, secondary = extract_diagonals(matrix_size=size_input, matrix_data=full_matrix)

    print(f'Primary diagonal: {", ".join([str(el) for el in primary])}. Sum: {sum(primary)}')
    print(f'Secondary diagonal: {", ".join([str(el) for el in secondary])}. Sum: {sum(secondary)}')
