import re


def match_dates(text: str) -> list[str]:
    """
    Matches valid dates in the format "dd{separator}MMM{separator}yyyy" from a given text.

    :param text: The input text containing dates.
    :return: A list of matched dates with their components.
    """
    regex_pattern = r'\b(\d{2})([./-])([A-Z][a-z]{2})\2(\d{4})\b'

    matches = re.findall(regex_pattern, text)

    return [f'Day: {match[0]}, Month: {match[2]}, Year: {match[3]}' for match in matches]


if __name__ == '__main__':
    input_text = input()
    matched_dates = match_dates(text=input_text)
    for date in matched_dates:
        print(date)
