import re


def extract_valid_numbers(numbers: str) -> list[str]:
    """Extracts valid integer and decimal numbers, ensuring no invalid leading zeros (like 00000.3)."""
    pattern = r'(?:(?<=\s)|^)-?(?:0|[1-9]\d*)(\.\d+)?(?=\s|$)'

    valid_numbers = [match.group() for match in re.finditer(pattern, numbers)]

    return valid_numbers


if __name__ == '__main__':
    numbers_input: str = input().strip()

    valid_nums: list[str] = extract_valid_numbers(numbers_input)

    print(' '.join(valid_nums))
