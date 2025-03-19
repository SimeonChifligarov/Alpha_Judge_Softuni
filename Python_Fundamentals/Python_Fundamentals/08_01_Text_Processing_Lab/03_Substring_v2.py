def remove_substring():
    to_be_removed = input().strip()
    string = input().strip()

    while to_be_removed in string:
        string = string.replace(to_be_removed, '')

    print(string)


if __name__ == '__main__':
    remove_substring()
