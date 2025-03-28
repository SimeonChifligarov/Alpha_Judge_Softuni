import re


def match_full_names(text: str) -> list[str]:
    """
    Matches full names from a sequence of characters based on given conditions.

    :param text: The input text containing names.
    :return: A list of matched full names.
    """
    regex_pattern = r'\b[A-Z][a-z]+ [A-Z][a-z]+\b'
    return re.findall(regex_pattern, text)


if __name__ == '__main__':
    input_text = input()
    matched_names = match_full_names(text=input_text)
    print(' '.join(matched_names))
