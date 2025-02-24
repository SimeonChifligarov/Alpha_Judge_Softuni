def remove_vowels(text: str) -> str:
    """
    Removes all vowels (a, o, u, e, i) from the given text, case insensitive.
    """
    return ''.join([ch for ch in text if ch.lower() not in {'a', 'o', 'u', 'e', 'i'}])


if __name__ == '__main__':
    text_input = input()
    result_text = remove_vowels(text=text_input)
    print(result_text)
