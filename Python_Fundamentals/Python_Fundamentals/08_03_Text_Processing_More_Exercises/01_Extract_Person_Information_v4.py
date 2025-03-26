def extract_name_age(lines: list[str]) -> list[str]:
    """
    Extracts the name and age from given lines and returns formatted results.

    :param lines: List of input strings containing name and age information.
    :return: List of formatted strings containing name-age pairs.
    """
    return [f"{line.split('@')[1].split('|')[0]} is {line.split('#')[1].split('*')[0]} years old." for line in lines]


if __name__ == '__main__':
    n = int(input())
    input_lines = [input() for _ in range(n)]
    results = extract_name_age(lines=input_lines)
    for result in results:
        print(result)
