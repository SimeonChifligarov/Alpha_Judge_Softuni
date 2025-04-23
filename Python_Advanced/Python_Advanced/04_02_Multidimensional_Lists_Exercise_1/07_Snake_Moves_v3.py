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
    result = []
    index = 0
    length = len(snake_text)

    for r in range(row_count):
        row = [snake_text[index % length] for index in range(index, index + column_count)]
        index += column_count
        if r % 2 == 1:
            row.reverse()
        result.append(row)

    return result


if __name__ == '__main__':
    total_rows, total_columns = [int(x) for x in input().split()]
    snake_string = input()

    matrix = create_snake_path(row_count=total_rows, column_count=total_columns, snake_text=snake_string)

    for c_row in matrix:
        print(''.join(c_row))
