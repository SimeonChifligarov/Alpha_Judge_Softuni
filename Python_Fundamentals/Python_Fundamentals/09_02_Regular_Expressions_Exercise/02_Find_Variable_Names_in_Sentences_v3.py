import re


def extract_variable_names(line_data: str) -> list[str]:
    """Extracts variable names that start with an underscore (_) but are not preceded by another character."""
    pattern = r'(?<=\b_)[a-zA-Z0-9]+\b'

    return [match.group() for match in re.finditer(pattern, line_data)]


if __name__ == '__main__':
    line_input: str = input().strip()

    var_names: list[str] = extract_variable_names(line_input)
    print(','.join(var_names))
