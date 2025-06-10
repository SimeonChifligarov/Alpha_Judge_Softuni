from typing import Generator


def squares(n: int) -> Generator[int, None, None]:
    """
    This function generates squares of numbers from 1 to n (inclusive).

    Args:
        n (int): The upper limit number.

    Yields:
        int: The square of each number from 1 to n.
    """
    number = 1
    while number <= n:
        yield number * number
        number += 1


if __name__ == '__main__':
    # print(list(squares(n=5)))
    pass
