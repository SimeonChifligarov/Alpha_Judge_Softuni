def compute_result(tokens: list[str]) -> int:
    """
    This function reads a math expression and finds the answer step by step.

    Args:
        tokens (list[str]): List with numbers and operators as strings.

    Returns:
        int: The answer after finishing the calculation.
    """
    actions = {
        '*': lambda values: multiply_all(values),
        '+': lambda values: add_all(values),
        '-': lambda values: subtract_all(values),
        '/': lambda values: divide_all(values),
    }
    numbers = []
    for token in tokens:
        if token in actions:
            numbers = [actions[token](numbers)]
        else:
            numbers.append(int(token))
    return numbers[0]


def multiply_all(values: list[int]) -> int:
    """
    This function multiplies all numbers in a list.

    Args:
        values (list[int]): List of numbers.

    Returns:
        int: The product of all numbers.
    """
    result = values[0]
    for value in values[1:]:
        result *= value
    return result


def add_all(values: list[int]) -> int:
    """
    This function adds all numbers in a list.

    Args:
        values (list[int]): List of numbers.

    Returns:
        int: The sum of all numbers.
    """
    result = values[0]
    for value in values[1:]:
        result += value
    return result


def subtract_all(values: list[int]) -> int:
    """
    This function subtracts all numbers in a list from the first number.

    Args:
        values (list[int]): List of numbers.

    Returns:
        int: The result after all subtractions.
    """
    result = values[0]
    for value in values[1:]:
        result -= value
    return result


def divide_all(values: list[int]) -> int:
    """
    This function divides the first number by all others one by one.

    Args:
        values (list[int]): List of numbers.

    Returns:
        int: The result after all divisions rounded down.
    """
    result = values[0]
    for value in values[1:]:
        result //= value
    return result


if __name__ == '__main__':
    data_input = input().split()
    answer = compute_result(tokens=data_input)
    print(answer)
