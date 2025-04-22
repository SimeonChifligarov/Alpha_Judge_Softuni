def generate_palindrome_matrix(row_count: int, column_count: int) -> list[list[str]]:
    """
    This function makes a matrix of 3-letter palindromes using letter positions.

    Args:
    row_count: how many rows to create
    column_count: how many columns to create

    Returns:
    A matrix where each cell is a 3-letter palindrome
    """
    result_matrix = []

    for row in range(row_count):
        current_row = []
        for col in range(column_count):
            outer = chr(97 + row)
            middle = chr(97 + row + col)
            palindrome = outer + middle + outer
            current_row.append(palindrome)
        result_matrix.append(current_row)

    return result_matrix


if __name__ == '__main__':
    size_data = input().split()
    total_rows = int(size_data[0])
    total_columns = int(size_data[1])

    palindrome_matrix = generate_palindrome_matrix(row_count=total_rows, column_count=total_columns)

    for r in palindrome_matrix:
        print(' '.join(r))
