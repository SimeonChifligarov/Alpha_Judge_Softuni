import re


def match_dates(text: str) -> list[str]:
    """
    Matches valid dates in the format "dd{separator}MMM{separator}yyyy" from a given text.

    :param text: The input text containing dates.
    :return: A list of matched dates with their components.
    """
    regex_pattern = r'\b(\d{2})([./-])([A-Z][a-z]{2})\2(\d{4})\b'

    matches = re.findall(regex_pattern, text)

    extracted_dates = []
    for day, separator, month, year in matches:
        extracted_dates.append(f'Day: {day}, Month: {month}, Year: {year}')

    return extracted_dates


if __name__ == '__main__':
    input_text = input()
    matched_dates = match_dates(text=input_text)
    for date in matched_dates:
        print(date)
