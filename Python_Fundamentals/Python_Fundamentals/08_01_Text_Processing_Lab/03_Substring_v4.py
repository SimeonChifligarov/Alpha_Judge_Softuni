def remove_occurrences(substring: str, main_string: str) -> str:
    """
    Removes all occurrences of the substring from the main string until no matches remain.
    Returns the modified string.
    """
    while substring in main_string:
        main_string = main_string.replace(substring, '')
    return main_string


if __name__ == '__main__':
    substring_input: str = input()
    main_string_input: str = input()
    result: str = remove_occurrences(substring=substring_input, main_string=main_string_input)
    print(result)
