def get_even_length_words(text: str) -> list[str]:
    """
    Returns a list of words with even length from the given text.
    """
    return [word for word in text.split() if len(word) % 2 == 0]


if __name__ == '__main__':
    text_input = input()
    even_words = get_even_length_words(text=text_input)
    print('\n'.join(even_words))
