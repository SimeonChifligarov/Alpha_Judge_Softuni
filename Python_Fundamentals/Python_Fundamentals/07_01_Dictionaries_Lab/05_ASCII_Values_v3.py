def create_ascii_dict(characters: list[str]) -> dict[str, int]:
    """Creates a dictionary mapping characters to their ASCII values."""
    return {char: ord(char) for char in characters}


if __name__ == '__main__':
    char_list = input().split(', ')
    ascii_dict = create_ascii_dict(characters=char_list)
    print(ascii_dict)
