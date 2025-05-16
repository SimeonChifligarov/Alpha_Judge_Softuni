def print_rhombus(size: int) -> None:
    """
    Print a rhombus of stars with given size.

    Args:
        size: number of rows in the upper half of the rhombus

    Returns:
        None
    """
    for row in range(1, size + 1):
        spaces = ' ' * (size - row)
        stars = ' '.join(['*'] * row)
        print(f'{spaces}{stars}')

    for row in range(size - 1, 0, -1):
        spaces = ' ' * (size - row)
        stars = ' '.join(['*'] * row)
        print(f'{spaces}{stars}')


if __name__ == '__main__':
    input_size = int(input())
    print_rhombus(size=input_size)
