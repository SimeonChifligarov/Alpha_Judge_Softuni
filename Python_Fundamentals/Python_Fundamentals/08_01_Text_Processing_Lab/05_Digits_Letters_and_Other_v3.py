def separate_characters(string: str) -> tuple[str, str, str]:
    """Separates digits, letters, and other characters from `string`."""
    all_digits, all_letters, all_others = [], [], []

    for char in string:
        if char.isdigit():
            all_digits.append(char)
        elif char.isalpha():
            all_letters.append(char)
        else:
            all_others.append(char)

    return ''.join(all_digits), ''.join(all_letters), ''.join(all_others)


if __name__ == '__main__':
    string_input: str = input().strip()

    digits, letters, others = separate_characters(string_input)

    print(digits)
    print(letters)
    print(others)
