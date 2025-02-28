def print_even_length_words(text: str) -> None:
    """
    Prints words with even length from the given text.
    """
    [print(word) for word in text.split() if len(word) % 2 == 0]


if __name__ == '__main__':
    text_input = input()
    print_even_length_words(text=text_input)
