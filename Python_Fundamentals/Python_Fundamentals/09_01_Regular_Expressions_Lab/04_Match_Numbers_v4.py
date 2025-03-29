import re


def find_numbers(text: str) -> list[str]:
    """
    Finds all integer and floating-point numbers in a given text.
    Ensures floating-point numbers do not have leading zeros unless they are "0.x".

    :param text: The input text containing numbers.
    :return: A list of matched numbers as strings.
    """
    regex_pattern = r'(^|(?<=\s))(?P<number>-?(?:0|[1-9]\d*)(?:\.\d+)?)(?=\s|$)'

    matches = re.finditer(regex_pattern, text)

    return [match.group('number') for match in matches]


if __name__ == '__main__':
    input_text = input()
    matched_numbers = find_numbers(text=input_text)
    print(' '.join(matched_numbers))
