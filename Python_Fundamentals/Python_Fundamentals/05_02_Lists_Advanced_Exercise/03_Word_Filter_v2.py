def filter_even_length_words(words: list[str]) -> None:
    """Prints words that have an even number of characters, each on a new line."""
    even_words = [word for word in words if len(word) % 2 == 0]
    print(*even_words, sep='\n')


if __name__ == '__main__':
    words_input = input().split()
    filter_even_length_words(words=words_input)
