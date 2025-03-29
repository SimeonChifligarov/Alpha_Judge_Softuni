import re


def find_numbers(text: str) -> list[str]:
    """
    Finds all integer and floating-point numbers in a given text.
    Ensures floating-point numbers do not have leading zeros unless they are "0.x".

    :param text: The input text containing numbers.
    :return: A list of matched numbers as strings.
    """
    regex_pattern = r'(^|(?<=\s))(-?(0|[1-9]\d*)(\.\d+)?)(?=\s|$)'

    matches = re.findall(regex_pattern, text)

    extracted_numbers = []
    for _, full_number, _, _ in matches:
        extracted_numbers.append(full_number)

    return extracted_numbers


if __name__ == '__main__':
    input_text = input()
    matched_numbers = find_numbers(text=input_text)
    print(' '.join(matched_numbers))
