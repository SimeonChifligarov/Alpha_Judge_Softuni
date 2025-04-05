import re


def extract_text_from_html(html: str) -> tuple[str, str]:
    """
    Extracts the title and content from an HTML string.
    Removes all HTML tags and replaces escaped newline, tab, and carriage return sequences.
    """
    title_regex = re.compile(r'<title>(.*?)</title>', re.VERBOSE | re.DOTALL)
    body_regex = re.compile(r'<body>(.*?)</body>', re.VERBOSE | re.DOTALL)
    tag_regex = re.compile(r'<.*?>', re.VERBOSE)
    whitespace_regex = re.compile(r'\\n|\\t|\\r')

    title_match = title_regex.search(html)
    body_match = body_regex.search(html)

    title = title_match.group(1).strip() if title_match else ''
    body = body_match.group(1) if body_match else ''

    cleaned_body = tag_regex.sub(' ', body)
    cleaned_body = whitespace_regex.sub(' ', cleaned_body)
    formatted_content = ' '.join(cleaned_body.split()).strip()

    return title, formatted_content


def main() -> None:
    """Reads HTML input, extracts title and content, and prints the results."""
    html_input = input()
    title, content = extract_text_from_html(html=html_input)

    print(f'Title: {title}')
    print(f'Content: {content}')


if __name__ == '__main__':
    main()
