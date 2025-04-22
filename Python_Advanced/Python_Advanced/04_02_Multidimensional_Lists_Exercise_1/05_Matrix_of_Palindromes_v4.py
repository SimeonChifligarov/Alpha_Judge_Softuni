def generate_palindrome_matrix(row_count: int, column_count: int) -> list[list[str]]:
    """
    This function makes a matrix of 3-letter palindromes using letter positions.

    Args:
    row_count: how many rows to create
    column_count: how many columns to create

    Returns:
    A matrix where each cell is a 3-letter palindrome
    """
    return [[(base := chr(97 + row)) + chr(97 + row + col) + base for col in range(column_count)] for row in
            range(row_count)]


if __name__ == '__main__':
    total_rows, total_columns = [int(x) for x in input().split()]
    matrix = generate_palindrome_matrix(row_count=total_rows, column_count=total_columns)

    for r in matrix:
        print(' '.join(r))
