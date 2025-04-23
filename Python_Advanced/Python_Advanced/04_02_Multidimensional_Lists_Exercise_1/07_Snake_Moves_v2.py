def create_snake_path(row_count: int, column_count: int, snake_text: str) -> list[list[str]]:
    """
    This function fills a matrix with a snake string in a zigzag pattern.

    Args:
    row_count: how many rows the matrix has
    column_count: how many columns the matrix has
    snake_text: the string that represents the snake

    Returns:
    A matrix filled with the snake's path
    """
    result_matrix = []
    snake_index = 0
    snake_length = len(snake_text)

    for row in range(row_count):
        current_row = []
        for _ in range(column_count):
            current_row.append(snake_text[snake_index])
            snake_index = (snake_index + 1) % snake_length

        if row % 2 == 1:
            current_row.reverse()

        result_matrix.append(current_row)

    return result_matrix


if __name__ == '__main__':
    size_parts = input().split()
    total_rows = int(size_parts[0])
    total_columns = int(size_parts[1])

    snake_string = input()
    snake_matrix = create_snake_path(row_count=total_rows, column_count=total_columns, snake_text=snake_string)

    for r in snake_matrix:
        print(''.join(r))
