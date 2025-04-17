def solve_expression(elements: list[str]) -> int:
    """
    This function calculates a math expression using operations stored in a dictionary.

    Args:
        elements (list[str]): A list that has numbers and operators.

    Returns:
        int: The final calculated value.
    """
    operations = {
        '*': lambda a, b: a * b,
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '/': lambda a, b: a // b,
    }
    values = []
    for item in elements:
        if item in operations:
            outcome = values[0]
            for num in values[1:]:
                outcome = operations[item](outcome, num)
            values = [outcome]
        else:
            values.append(int(item))
    return values[0]


if __name__ == '__main__':
    input_expression = input().split()
    final_result = solve_expression(elements=input_expression)
    print(final_result)
