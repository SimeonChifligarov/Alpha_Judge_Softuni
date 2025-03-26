def extract_name_age(lines: list[str]) -> None:
    """
    Extracts and prints the name and age from given lines.

    :param lines: List of input strings containing name and age information.
    """
    for line in lines:
        name = line.split('@')[1].split('|')[0]
        age = line.split('#')[1].split('*')[0]
        print(f'{name} is {age} years old.')


if __name__ == '__main__':
    n = int(input())
    input_lines = [input() for _ in range(n)]
    extract_name_age(lines=input_lines)
