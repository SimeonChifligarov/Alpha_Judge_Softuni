import re


def extract_emails(text: str) -> list[str]:
    """Extracts all valid email addresses from `text` using regex."""
    pattern = (
        r'(^|(?<=\s))'
        r'[a-zA-Z0-9]+([\._-][a-zA-Z0-9]+)?'
        r'@[a-zA-Z]+(-[a-zA-Z]+)?'
        r'(\.[a-zA-Z]+(-[a-zA-Z]+)?)+'
    )

    return [match.group() for match in re.finditer(pattern, text)]


if __name__ == '__main__':
    text_input: str = input().strip()

    extracted_emails: list[str] = extract_emails(text_input)

    print('\n'.join(extracted_emails))
