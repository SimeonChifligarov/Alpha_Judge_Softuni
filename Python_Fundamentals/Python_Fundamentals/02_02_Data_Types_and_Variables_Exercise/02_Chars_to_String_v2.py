def concatenate_chars(char1: str, char2: str, char3: str) -> str:
    return char1 + char2 + char3


if __name__ == '__main__':
    first_char = input()
    second_char = input()
    third_char = input()
    result = concatenate_chars(char1=first_char, char2=second_char, char3=third_char)
    print(result)
