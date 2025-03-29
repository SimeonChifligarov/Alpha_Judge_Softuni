import re


def extract_valid_numbers(numbers: str) -> list[str]:
    """Extracts valid integer and decimal numbers, ignoring those starting with '00'."""
    pattern = r'(^|(?<=\s))-?\d+(\.\d+)?($|(?=\s))'

    valid_numbers = [
        match.group() for match in re.finditer(pattern, numbers)
        if not match.group().startswith('00')
    ]

    return valid_numbers


if __name__ == '__main__':
    numbers_input: str = input().strip()

    valid_numbers: list[str] = extract_valid_numbers(numbers_input)

    print(" ".join(valid_numbers))
