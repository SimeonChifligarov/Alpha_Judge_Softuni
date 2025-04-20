def find_symbol(matrix_size: int, matrix_data: list[list[str]], target_symbol: str) -> str:
    """
    This function looks for the first spot where a symbol appears in the matrix.

    Args:
    matrix_size: how many rows and columns the matrix has
    matrix_data: the matrix as a list of character lists
    target_symbol: the symbol to search for

    Returns:
    A string with the position of the symbol, or a message if not found
    """
    return next(
        (f'({i}, {j})' for i in range(matrix_size) for j in range(matrix_size) if matrix_data[i][j] == target_symbol),
        f'{target_symbol} does not occur in the matrix')


if __name__ == '__main__':
    matrix_size_input = int(input())
    character_matrix = [list(input()) for _ in range(matrix_size_input)]
    search_symbol = input()

    result = find_symbol(matrix_size=matrix_size_input, matrix_data=character_matrix, target_symbol=search_symbol)
    print(result)
