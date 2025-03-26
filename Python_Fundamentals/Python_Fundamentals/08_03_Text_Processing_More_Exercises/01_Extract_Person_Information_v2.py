def extract_name_and_age(data: str) -> tuple[str, str]:
    """Extracts name (between '@' and '|') and age (between '#' and '*') from a given string."""
    name_start = data.find('@') + 1
    name_end = data.find('|')
    age_start = data.find('#') + 1
    age_end = data.find('*')

    name = data[name_start:name_end]
    age = data[age_start:age_end]

    return name, age


if __name__ == '__main__':
    number_of_lines: int = int(input().strip())

    for _ in range(number_of_lines):
        data_input: str = input().strip()

        name, age = extract_name_and_age(data_input)
        print(f'{name} is {age} years old.')
