def censor_text(banned_words: str, text: str) -> str:
    """
    Replaces all occurrences of banned words in the text with asterisks (*) equal to their length.
    Returns the censored text.
    """
    banned_list: list[str] = banned_words.split(', ')
    for word in banned_list:
        text = text.replace(word, '*' * len(word))
    return text


if __name__ == '__main__':
    banned_words_input: str = input()
    text_input: str = input()
    result: str = censor_text(banned_words=banned_words_input, text=text_input)
    print(result)
