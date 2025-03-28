import re


def extract_valid_names(names: str) -> list[str]:
    """Extracts valid names in the format 'First Last' where both names start with an uppercase letter."""
    pattern = r'\b[A-Z][a-z]+ [A-Z][a-z]+\b'
    return re.findall(pattern, names)


if __name__ == '__main__':
    names_input: str = input().strip()

    valid_names: list[str] = extract_valid_names(names_input)
    print(*valid_names)
