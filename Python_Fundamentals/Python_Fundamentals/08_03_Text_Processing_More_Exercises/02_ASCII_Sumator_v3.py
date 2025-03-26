def sum_ascii_between_chars(start_char: str, end_char: str, text: str) -> int:
    """
    Calculates the sum of ASCII values of all characters in 'text' that are between
    'start_char' and 'end_char' in the ASCII table.

    :param start_char: The starting character.
    :param end_char: The ending character.
    :param text: The input string to process.
    :return: The sum of ASCII values of the characters within the given range.
    """
    start_ascii, end_ascii = ord(start_char), ord(end_char)

    return sum(ord(char) for char in text if start_ascii < ord(char) < end_ascii)


if __name__ == '__main__':
    char_1 = input()
    char_2 = input()
    random_string = input()

    result = sum_ascii_between_chars(start_char=char_1, end_char=char_2, text=random_string)
    print(result)
