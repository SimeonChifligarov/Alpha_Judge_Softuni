def draw_recursive(level: int) -> None:
    """
    Draw a pattern using recursion. First draw descending stars,
    then draw ascending hashes.

    Args:
        level: how many rows to draw

    Returns:
        None
    """
    if level == 0:
        return
    print('*' * level)
    draw_recursive(level=level - 1)
    print('#' * level)


if __name__ == '__main__':
    input_level = int(input())
    draw_recursive(level=input_level)
