import re


def extract_name_age(lines: list[str]) -> list[str]:
    """
    Extracts the name and age from given lines using regex and returns formatted results.

    :param lines: List of input strings containing name and age information.
    :return: List of formatted strings containing name-age pairs.
    """
    name_pattern = r'@([A-Za-z]+)\|'
    age_pattern = r'#(\d+)\*'

    return [
        f"{name} is {age} years old."
        for line in lines
        if (name_match := re.search(name_pattern, line)) and (age_match := re.search(age_pattern, line))
        if (name := name_match.group(1)) and (age := age_match.group(1))
    ]


if __name__ == '__main__':
    n = int(input())
    input_lines = [input() for _ in range(n)]
    results = extract_name_age(lines=input_lines)
    for result in results:
        print(result)
