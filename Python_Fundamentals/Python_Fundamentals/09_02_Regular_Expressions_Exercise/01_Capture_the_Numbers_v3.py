import re


def extract_numbers() -> str:
    """
    Reads input lines, extracts numbers using regex, and returns them as a space-separated string.
    """
    lines = []

    while True:
        line = input()
        if not line:
            break

        lines.append(line)

    return ' '.join(re.findall(r'\d+', ' '.join(lines)))


if __name__ == '__main__':
    result = extract_numbers()
    print(result)
