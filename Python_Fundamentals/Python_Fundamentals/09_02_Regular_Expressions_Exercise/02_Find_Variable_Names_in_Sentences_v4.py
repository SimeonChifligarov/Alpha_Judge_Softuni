import re


def extract_variable_names(line: str) -> str:
    """
    Reads input lines, extracts variable names using regex finditer, and returns them as a comma-separated string.
    """
    return ','.join([el.group() for el in re.finditer(r'((?<= _)|(?<=^_))[a-zA-Z0-9]+\b', line)])


if __name__ == '__main__':
    line_input: str = input()
    result: str = extract_variable_names(line=line_input)
    print(result)
