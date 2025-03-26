def sum_ascii_between_chars(start_char: str, end_char: str, text: str) -> int:
    """
    Calculates the sum of ASCII values of all characters in 'text' that are between
    'start_char' and 'end_char' in the ASCII table.

    :param start_char: The starting character.
    :param end_char: The ending character.
    :param text: The input string to process.
    :return: The sum of ASCII values of the characters within the given range.
    """
    start_ascii = ord(start_char)
    end_ascii = ord(end_char)

    ascii_sum = 0
    for char in text:
        char_ascii = ord(char)
        if start_ascii < char_ascii < end_ascii:
            ascii_sum += char_ascii

    return ascii_sum


if __name__ == '__main__':
    char_1 = input()
    char_2 = input()
    random_string = input()

    result = sum_ascii_between_chars(start_char=char_1, end_char=char_2, text=random_string)
    print(result)
