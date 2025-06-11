from typing import Generator


def genrange(start: int, end: int) -> Generator[int, None, None]:
    """
    This function generates numbers from start to end (inclusive).

    Args:
        start (int): The starting number.
        end (int): The ending number.

    Yields:
        int: Each number from start to end.
    """
    for number in range(start, end + 1):
        yield number


if __name__ == '__main__':
    # print(list(genrange(start=1, end=10)))
    pass
