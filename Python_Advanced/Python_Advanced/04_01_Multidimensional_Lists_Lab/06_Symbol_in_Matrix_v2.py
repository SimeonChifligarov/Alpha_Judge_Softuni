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
    for row_index in range(matrix_size):
        for col_index in range(matrix_size):
            if matrix_data[row_index][col_index] == target_symbol:
                return f'({row_index}, {col_index})'
    return f'{target_symbol} does not occur in the matrix'


if __name__ == '__main__':
    matrix_size_input = int(input())

    character_matrix = []
    for _ in range(matrix_size_input):
        row_data = list(input())
        character_matrix.append(row_data)

    search_symbol = input()
    result = find_symbol(matrix_size=matrix_size_input, matrix_data=character_matrix, target_symbol=search_symbol)
    print(result)
