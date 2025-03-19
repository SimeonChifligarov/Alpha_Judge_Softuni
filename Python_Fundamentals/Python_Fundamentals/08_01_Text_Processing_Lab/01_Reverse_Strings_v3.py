def reverse_strings() -> None:
    """
    Reads input strings until 'end' is encountered.
    For each string, prints the string and its reversed version.
    """
    while True:
        user_input: str = input()
        if user_input == 'end':
            break
        reversed_input: str = user_input[::-1]
        print(f'{user_input} = {reversed_input}')


if __name__ == '__main__':
    reverse_strings()
