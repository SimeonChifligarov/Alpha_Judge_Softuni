from itertools import zip_longest


def calculate_character_code_sum(string_1: str, string_2: str) -> int:
    """
    Calculates the sum of multiplied character codes for corresponding characters in two strings.
    If one string is longer, adds the remaining character codes without multiplication.
    """
    total_sum: int = sum(
        ord(a) * ord(b) if a and b else ord(a or b)
        for a, b
        in zip_longest(string_1, string_2, fillvalue='')
    )

    return total_sum


if __name__ == '__main__':
    input_string: str = input()
    str_1, str_2 = input_string.split()
    result: int = calculate_character_code_sum(string_1=str_1, string_2=str_2)
    print(result)
