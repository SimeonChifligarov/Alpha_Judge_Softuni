import re


def extract_html_data(html_input: str) -> tuple[str, str]:
    """
    Extracts the title and content from an HTML string.
    Removes all HTML tags and replaces escaped newlines, tabs, and carriage returns.
    """
    title_pattern = re.compile(r'<title>(.*?)</title>', re.VERBOSE | re.DOTALL)
    body_pattern = re.compile(r'<body>(.*?)</body>', re.VERBOSE | re.DOTALL)
    tag_pattern = re.compile(r'<.*?>', re.VERBOSE)
    new_line_pattern = re.compile(r'\\n|\\t|\\r')

    title_match = title_pattern.search(html_input)
    body_match = body_pattern.search(html_input)

    title = title_match.group(1).strip() if title_match else ''
    body = body_match.group(1) if body_match else ''

    clean_body = tag_pattern.sub(' ', body)

    clean_body = new_line_pattern.sub(' ', clean_body)

    formatted_content = ' '.join(clean_body.split()).strip()

    return title, formatted_content


if __name__ == '__main__':
    html_input = input()
    extracted_title, extracted_content = extract_html_data(html_input=html_input)

    print(f'Title: {extracted_title}')
    print(f'Content: {extracted_content}')
