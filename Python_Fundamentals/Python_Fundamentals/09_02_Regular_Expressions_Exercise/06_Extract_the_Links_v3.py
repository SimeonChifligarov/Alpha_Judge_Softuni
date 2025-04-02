import re


def extract_valid_urls() -> list[str]:
    """Extracts valid website URLs in the format 'www.domain.tld' from multiple input lines."""
    pattern = r'\bw{3}\.[a-zA-Z0-9-]+(\.[a-z]+)+'
    all_urls = []

    while True:
        current_line = input().strip()
        if not current_line:
            break

        all_urls.extend(match.group() for match in re.finditer(pattern, current_line))

    return all_urls


if __name__ == '__main__':
    extracted_urls: list[str] = extract_valid_urls()

    print('\n'.join(extracted_urls))
