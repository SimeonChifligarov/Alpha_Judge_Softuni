import re


def extract_emails(text: str) -> list[str]:
    """
    Extracts all valid email addresses from the given text using named groups and returns them as a list.
    """
    pattern = (
        r'(?:(?<=\s)|(?<=^))'
        r'(?P<user>[a-zA-Z0-9]+(?:[\._-][a-zA-Z0-9]+)*)@'
        r'(?P<host>[a-zA-Z]+(?:-[a-zA-Z]+)?(?:\.[a-zA-Z]+(?:-[a-zA-Z]+)?)+)'
    )

    return [match.group() for match in re.finditer(pattern, text)]


if __name__ == '__main__':
    input_text = input().strip()

    result = extract_emails(text=input_text)
    for email in result:
        print(email)
