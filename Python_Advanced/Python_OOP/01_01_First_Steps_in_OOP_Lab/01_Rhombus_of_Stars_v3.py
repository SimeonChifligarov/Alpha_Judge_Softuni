def print_rhombus(size: int) -> None:
    """
    Create rhombus from stars.

    Args:
        size: height of top half

    Returns:
        None
    """
    for i in range(1, size + 1):
        print(' ' * (size - i) + ' '.join(['*'] * i))
    for i in range(size - 1, 0, -1):
        print(' ' * (size - i) + ' '.join(['*'] * i))


if __name__ == '__main__':
    input_size = int(input())
    print_rhombus(size=input_size)
