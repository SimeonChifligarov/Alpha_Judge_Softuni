def get_char_occurrences(given_text: str) -> dict:
    """
    This function counts the times every character shows up.

    Args:
        given_text (str): The text to look at

    Returns:
        dict: A dictionary with character counts
    """
    char_map = {ch: given_text.count(ch) for ch in sorted(set(given_text))}
    return char_map


if __name__ == '__main__':
    input_text_value = input()
    result_occurrences = get_char_occurrences(given_text=input_text_value)
    for character, count in result_occurrences.items():
        print(f'{character}: {count} time/s')
