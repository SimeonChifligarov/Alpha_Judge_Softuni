import re


def extract_emails(text: str) -> list[str]:
    """
    Extracts all valid email addresses from the given text and returns them as a list.
    """
    pattern = r'(?:(?<=\s)|(?<=^))[a-zA-Z0-9]+(?:[\._-][a-zA-Z0-9]+)*@[a-zA-Z]+(?:-[a-zA-Z]+)?(?:\.[a-zA-Z]+(?:-[a-zA-Z]+)?)+'  # noqa
    return re.findall(pattern, text)


if __name__ == '__main__':
    input_text = input().strip()

    result = extract_emails(text=input_text)
    for email in result:
        print(email)
