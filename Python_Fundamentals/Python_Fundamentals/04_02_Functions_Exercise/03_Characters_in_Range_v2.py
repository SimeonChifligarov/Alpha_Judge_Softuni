def get_chars_in_between(char_1: str, char_2: str) -> str:
    """
    Returns a string containing all characters between the two given characters in ASCII order, separated by a space.
    """
    return ' '.join(chr(i) for i in range(ord(char_1) + 1, ord(char_2)))


if __name__ == '__main__':
    first_char = input()
    second_char = input()
    result = get_chars_in_between(char_1=first_char, char_2=second_char)
    print(result)
