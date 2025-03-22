def find_emoticons(text: str) -> list[str]:
    """
    Finds all emoticons in the given text.
    An emoticon starts with ':' and is followed by a single alphanumeric character or ')' or '('.
    Returns a list of emoticons found.
    """
    emoticons: list[str] = []

    for index in range(len(text) - 1):
        current_char: str = text[index]
        next_char: str = text[index + 1]

        # if current_char == ':' and (next_char.isalnum() or next_char in '()'):
        if current_char == ':':
            emoticon: str = current_char + next_char
            emoticons.append(emoticon)

    return emoticons


if __name__ == '__main__':
    user_input: str = input()
    emoticons_result: list[str] = find_emoticons(text=user_input)
    print('\n'.join(emoticons_result))
