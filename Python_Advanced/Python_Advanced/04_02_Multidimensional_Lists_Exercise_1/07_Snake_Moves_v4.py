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
    return [
        ([snake_text[(r * column_count + c) % len(snake_text)] for c in range(column_count)][::-1] if r % 2 else
         [snake_text[(r * column_count + c) % len(snake_text)] for c in range(column_count)])
        for r in range(row_count)
    ]


if __name__ == '__main__':
    total_rows, total_columns = [int(x) for x in input().split()]
    snake_string = input()

    matrix = create_snake_path(row_count=total_rows, column_count=total_columns, snake_text=snake_string)

    for c_row in matrix:
        print(''.join(c_row))
