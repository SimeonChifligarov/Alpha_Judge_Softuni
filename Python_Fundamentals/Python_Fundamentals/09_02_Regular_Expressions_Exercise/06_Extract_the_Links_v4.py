import re


def extract_valid_links(text: str) -> list[str]:
    """
    Extracts valid links from the given text using regex and returns them as a list.
    """
    pattern = r'\bwww\.[a-zA-Z0-9-]+\.[a-z]+(?:\.[a-z]+)*\b'
    return re.findall(pattern, text)


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
