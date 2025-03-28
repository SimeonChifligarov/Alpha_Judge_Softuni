import re


def extract_valid_phone_numbers(phone_numbers: str) -> list[str]:
    """Extracts valid Bulgarian phone numbers in the format '+359 2 XXX XXXX' or '+359-2-XXX-XXXX'."""
    pattern = r'(^|(?<=\s))\+359( |-)2\2\d{3}\2\d{4}\b'
    return [match.group() for match in re.finditer(pattern, phone_numbers)]


if __name__ == '__main__':
    phone_numbers_input: str = input().strip()

    valid_phone_numbers: list[str] = extract_valid_phone_numbers(phone_numbers_input)
    print(', '.join(valid_phone_numbers))
