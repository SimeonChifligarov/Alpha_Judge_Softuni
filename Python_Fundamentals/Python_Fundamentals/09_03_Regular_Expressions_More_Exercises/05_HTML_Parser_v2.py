import re


def extract_text(pattern: str, text: str) -> str:
    """Extracts text content based on a regex pattern."""
    match = re.search(pattern, text)
    return match.group(0).strip() if match else ''


def clean_text(text: str) -> str:
    """Removes HTML tags and newlines (\n, \t, \r) from text."""
    text = re.sub(r'<[^>]+>', '', text)
    new_line_pattern = r'\\n|\\t|\\r'
    text = re.sub(new_line_pattern, '', text)
    return text.strip()


def main():
    """Main function to extract and print the title and body content."""
    html_data = input()

    title = extract_text(r'(?<=<title>).*?(?=</title>)', html_data)
    title_cleaned = clean_text(title)
    print(f'Title: {title_cleaned}')

    body = extract_text(r'(?<=<body>).*?(?=</body>)', html_data)
    body_cleaned = clean_text(body)
    print(f'Content: {body_cleaned}')


if __name__ == '__main__':
    main()
