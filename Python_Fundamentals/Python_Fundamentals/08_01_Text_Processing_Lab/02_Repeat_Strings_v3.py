def repeat_strings(input_string: str) -> str:
    """
    Repeats each word in the input string N times, where N is the length of the word.
    Returns the concatenated result.
    """
    return ''.join([word * len(word) for word in input_string.split()])


if __name__ == '__main__':
    user_input: str = input()
    result: str = repeat_strings(input_string=user_input)
    print(result)
