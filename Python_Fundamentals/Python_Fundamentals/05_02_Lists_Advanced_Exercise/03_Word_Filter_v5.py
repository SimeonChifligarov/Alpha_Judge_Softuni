def get_even_length_words(words: list[str]) -> list[str]:
    """
    Returns a list of words with even length from the given list.
    """
    return [word for word in words if len(word) % 2 == 0]


if __name__ == '__main__':
    words_input = input().split()
    even_words = get_even_length_words(words=words_input)
    print('\n'.join(even_words))
