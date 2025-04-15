def count_characters(input_text: str) -> dict:
    """
    This function counts how many times each character appears.

    Args:
        input_text (str): The text to check

    Returns:
        dict: A dictionary with characters and how many times they appear
    """
    char_counter = {}
    for symbol in input_text:
        if symbol not in char_counter:
            char_counter[symbol] = 0
        char_counter[symbol] += 1
    return dict(sorted(char_counter.items()))


if __name__ == '__main__':
    text_input = input()
    character_counts = count_characters(input_text=text_input)
    for letter, times in character_counts.items():
        print(f'{letter}: {times} time/s')
