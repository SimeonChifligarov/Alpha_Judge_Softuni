def count_characters(input_str: str) -> None:
    """
    Counts and prints occurrences of all characters in a string except spaces.
    """
    char_count = {ch: input_str.count(ch) for ch in input_str if ch != ' '}
    for ch, count in char_count.items():
        print(f'{ch} -> {count}')


if __name__ == '__main__':
    user_input = input()
    count_characters(input_str=user_input)
