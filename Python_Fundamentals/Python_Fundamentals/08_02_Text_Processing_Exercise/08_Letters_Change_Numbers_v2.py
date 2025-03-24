def calculate_string_value(data: list[str]) -> float:
    """Processes a list of formatted strings, performing mathematical operations based on letter positions."""
    alphabet_order = {chr(num + 96): num for num in range(1, 27)}
    total_sum = 0

    for el in data:
        number = int(el[1:-1])
        current_result = 0

        if el[0].isupper():
            position = alphabet_order[el[0].lower()]
            current_result = number / position
        elif el[0].islower():
            position = alphabet_order[el[0]]
            current_result = number * position

        if el[-1].isupper():
            position = alphabet_order[el[-1].lower()]
            current_result -= position
        elif el[-1].islower():
            position = alphabet_order[el[-1]]
            current_result += position

        total_sum += current_result

    return total_sum


if __name__ == '__main__':
    data_input: list[str] = input().split()

    result: float = calculate_string_value(data_input)
    print(f'{result:.2f}')
