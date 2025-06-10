from typing import Generator


def squares(n: int) -> Generator[int, None, None]:
    """
    This function generates squares of numbers from 1 to n (inclusive).

    Args:
        n (int): The upper limit number.

    Yields:
        int: The square of each number from 1 to n.
    """
    for number in range(1, n + 1):
        yield number * number


if __name__ == '__main__':
    # print(list(squares(n=5)))
    pass
