def repeat_strings(input_string: str) -> str:
    """
    Repeats each word in the input string N times, where N is the length of the word.
    Returns the concatenated result.
    """
    words: list[str] = input_string.split()
    repeated_words: list[str] = [word * len(word) for word in words]
    concatenated_result: str = ''.join(repeated_words)
    return concatenated_result


if __name__ == '__main__':
    user_input: str = input()
    result: str = repeat_strings(input_string=user_input)
    print(result)
