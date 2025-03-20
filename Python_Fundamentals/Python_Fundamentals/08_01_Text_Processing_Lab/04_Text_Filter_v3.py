def censor_text(ban_list: list[str], text: str) -> str:
    """Replaces all occurrences of words in `ban_list` with asterisks in `text`."""
    for banned_word in ban_list:
        text = text.replace(banned_word, '*' * len(banned_word))
    return text


if __name__ == '__main__':
    ban_list_input: list[str] = input().split(', ')
    text_input: str = input().strip()

    result: str = censor_text(ban_list=ban_list_input, text=text_input)
    print(result)
