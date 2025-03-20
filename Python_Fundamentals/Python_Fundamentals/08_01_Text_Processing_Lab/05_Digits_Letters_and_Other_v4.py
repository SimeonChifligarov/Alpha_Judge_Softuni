def categorize_characters(input_string: str) -> tuple[str, str, str]:
    """
    Categorizes characters in the input string into digits, letters, and others.
    Returns a tuple containing three strings: digits, letters, and other characters.
    """
    digits: str = ''.join([char for char in input_string if char.isdigit()])
    letters: str = ''.join([char for char in input_string if char.isalpha()])
    others: str = ''.join([char for char in input_string if not char.isalnum()])
    return digits, letters, others


if __name__ == '__main__':
    user_input: str = input()
    digits_result, letters_result, others_result = categorize_characters(input_string=user_input)

    print(digits_result)
    print(letters_result)
    print(others_result)
