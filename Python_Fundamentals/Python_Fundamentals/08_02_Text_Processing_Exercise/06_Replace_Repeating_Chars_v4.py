def remove_consecutive_duplicates(text: str) -> str:
    """Removes consecutive duplicate letters from a string."""
    filtered_chars = []

    for index in range(len(text)):
        is_first_character = index == 0
        is_different_from_previous = text[index] != text[index - 1]

        if is_first_character or is_different_from_previous:
            filtered_chars.append(text[index])

    return ''.join(filtered_chars)


if __name__ == '__main__':
    input_text = input()
    result_text = remove_consecutive_duplicates(text=input_text)
    print(result_text)
