def calculate_character_code_sum(string_1: str, string_2: str) -> int:
    """
    Calculates the sum of multiplied character codes for corresponding characters in two strings.
    If one string is longer, adds the remaining character codes without multiplication.
    """
    min_length: int = min(len(string_1), len(string_2))
    total_sum: int = sum(ord(string_1[i]) * ord(string_2[i]) for i in range(min_length))

    total_sum += sum(ord(char) for char in string_1[min_length:])
    total_sum += sum(ord(char) for char in string_2[min_length:])

    return total_sum


if __name__ == '__main__':
    input_string: str = input()
    str_1, str_2 = input_string.split()
    result: int = calculate_character_code_sum(string_1=str_1, string_2=str_2)
    print(result)
