import re


def extract_numbers_from_lines() -> list[str]:
    """Reads multiple lines and extracts all numbers using regex."""
    pattern = r'\d+'
    all_numbers = []

    while True:
        line_data = input().strip()
        if not line_data:
            break

        all_numbers.extend(re.findall(pattern, line_data))

    return all_numbers


if __name__ == '__main__':
    extracted_numbers: list[str] = extract_numbers_from_lines()
    print(' '.join(extracted_numbers))
