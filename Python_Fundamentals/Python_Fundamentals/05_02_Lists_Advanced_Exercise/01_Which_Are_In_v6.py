def find_substrings(seq_1: list[str], seq_2: list[str]) -> list[str]:
    """
    Returns a list of strings from seq_1 that are substrings of any string in seq_2.
    """
    return [el for el in seq_1 if any(el in word for word in seq_2)]


if __name__ == '__main__':
    seq_1_input = input().split(', ')
    seq_2_input = input().split(', ')
    result = find_substrings(seq_1=seq_1_input, seq_2=seq_2_input)
    print(result)
