import re


def extract_valid_links(text: str) -> list[str]:
    """
    Extracts valid links from the given text using regex with named groups and returns them as a list.
    """
    pattern = (r'\b(?P<subdomain>www)\.'
               r'(?P<domain>[a-zA-Z0-9-]+)\.'
               r'(?P<extension>[a-z]+(?:\.[a-z]+)*)\b')

    return [match.group() for match in re.finditer(pattern, text)]


if __name__ == '__main__':
    input_text = []

    while True:
        line = input().strip()
        if not line:
            break
        input_text.append(line)

    full_text = ' '.join(input_text)
    result = extract_valid_links(text=full_text)

    for link in result:
        print(link)
