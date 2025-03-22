def find_emoticons(text: str) -> list[str]:
    """
    Finds all emoticons in the given text.
    An emoticon starts with ':' and is followed by a single symbol.
    Returns a list of emoticons found.
    """
    # return [
    #     text[i:i + 2] for i in range(len(text) - 1)
    #     if text[i] == ':' and (text[i + 1].isalnum() or text[i + 1] in '()')
    # ]
    return [text[i:i + 2] for i in range(len(text) - 1) if text[i] == ':']


if __name__ == '__main__':
    user_input: str = input()

    emoticons: list[str] = find_emoticons(text=user_input)
    print('\n'.join(emoticons))
