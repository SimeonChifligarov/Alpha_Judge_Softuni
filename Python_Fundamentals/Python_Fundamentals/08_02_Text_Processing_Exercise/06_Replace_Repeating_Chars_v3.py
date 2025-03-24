def remove_consecutive_duplicates(string: str) -> str:
    """Removes consecutive duplicate characters from `string`."""
    string_as_list = list(string)

    for i in range(len(string) - 1, 0, -1):
        if string[i] == string[i - 1]:
            string_as_list.pop(i)

    return ''.join(string_as_list)


if __name__ == '__main__':
    string_input: str = input().strip()

    result: str = remove_consecutive_duplicates(string_input)
    print(result)
