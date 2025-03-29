import re


def extract_valid_dates(dates: str) -> list[str]:
    """Extracts and formats valid dates in 'DD-MM-YYYY', 'DD.MM.YYYY', or 'DD/MM/YYYY' format."""
    pattern = r'\b(?P<Day>\d{2})(?P<Separator>[-.\/])(?P<Month>[A-Z][a-z]{2})(?P=Separator)(?P<Year>\d{4})\b'

    formatted_dates = [
        f"Day: {match.group('Day')}, Month: {match.group('Month')}, Year: {match.group('Year')}"
        for match in re.finditer(pattern, dates)
    ]

    return formatted_dates


if __name__ == '__main__':
    dates_input: str = input().strip()

    valid_dates: list[str] = extract_valid_dates(dates_input)

    print("\n".join(valid_dates))
