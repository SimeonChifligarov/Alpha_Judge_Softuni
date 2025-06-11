from typing import Generator


def reverse_text(text: str) -> Generator[str, None, None]:
    """
    This function generates characters of a string in reversed order.

    Args:
        text (str): The input string.

    Yields:
        str: Each character from the string, starting from the end.
    """
    for index in range(len(text) - 1, -1, -1):
        yield text[index]


if __name__ == '__main__':
    # for char in reverse_text(text='step'):
    #     print(char, end='')
    pass
