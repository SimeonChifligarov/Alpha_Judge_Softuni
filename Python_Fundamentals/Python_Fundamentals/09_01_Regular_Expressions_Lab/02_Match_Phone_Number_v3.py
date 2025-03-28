import re


def match_sofia_phone_numbers(text: str) -> list[str]:
    """
    Matches valid Sofia phone numbers from a given text.

    :param text: The input text containing phone numbers and other symbols.
    :return: A list of matched phone numbers.
    """
    regex_pattern = r'(^|(?<=\s))\+359 2 \d{3} \d{4}\b|(^|(?<=\s))\+359-2-\d{3}-\d{4}\b'
    return [el.group() for el in re.finditer(regex_pattern, text)]


if __name__ == '__main__':
    input_text = input()
    matched_numbers = match_sofia_phone_numbers(text=input_text)
    print(', '.join(matched_numbers))
