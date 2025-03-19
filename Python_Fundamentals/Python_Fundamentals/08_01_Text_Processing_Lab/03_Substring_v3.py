def remove_substring(to_be_removed: str, string: str) -> str:
    """Removes all occurrences of `to_be_removed` from `string` until none remain."""
    while to_be_removed in string:
        string = string.replace(to_be_removed, '')
    return string


if __name__ == '__main__':
    to_be_removed_input: str = input().strip()
    string_input: str = input().strip()

    result: str = remove_substring(to_be_removed=to_be_removed_input, string=string_input)
    print(result)
