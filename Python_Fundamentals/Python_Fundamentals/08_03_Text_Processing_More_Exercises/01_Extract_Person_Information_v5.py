import re


def extract_name_age(lines: list[str]) -> list[str]:
    """
    Extracts the name and age from given lines using regex and returns formatted results.

    :param lines: List of input strings containing name and age information.
    :return: List of formatted strings containing name-age pairs.
    """
    # regex_pattern = r'@(?P<name>[A-Za-z]+)\|.*?#(?P<age>\d+)\*'  # TODO check this one
    # regex_pattern = r'@(?P<name>[A-Za-z]+)\|\D*?#(?P<age>\d+)\*'  # TODO check this one
    # regex_pattern = r'@(?P<name>[A-Za-z]+)\|[^@#]*#(?P<age>\d+)\*'  # TODO check this one
    regex_pattern = r'@(?P<name>[A-Za-z]+)\|.*#(?P<age>\d+)\*'
    return [f"{match.group('name')} is {match.group('age')} years old."
            for line in lines if (match := re.search(regex_pattern, line))]


if __name__ == '__main__':
    n = int(input())
    input_lines = [input() for _ in range(n)]
    results = extract_name_age(lines=input_lines)
    for result in results:
        print(result)
