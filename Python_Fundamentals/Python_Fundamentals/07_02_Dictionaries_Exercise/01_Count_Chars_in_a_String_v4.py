def count_characters(input_str: str) -> dict[str, int]:
    """
    Counts occurrences of all characters in a string except spaces.
    """
    return {ch: input_str.count(ch) for ch in input_str if ch != ' '}


def print_character_counts(char_counts: dict[str, int]) -> None:
    """
    Prints character occurrences in the required format.
    """
    for ch, count in char_counts.items():
        print(f'{ch} -> {count}')


if __name__ == '__main__':
    user_input = input()
    result = count_characters(input_str=user_input)
    print_character_counts(char_counts=result)
