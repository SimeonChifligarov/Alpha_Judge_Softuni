from functools import reduce


def operate(operator: str, *numbers: int) -> float:
    """
    This function applies a math operation using lambdas and numbers.

    Args:
        operator (str): The math symbol to use.
        *numbers (int): All numbers for the operation.

    Returns:
        float: The result after the operation.
    """

    def divide(values: tuple[int, ...]) -> float:
        result = values[0]
        for value in values[1:]:
            if value == 0:
                continue
            result /= value
        return result

    actions = {
        '+': lambda: sum(numbers),
        '-': lambda: numbers[0] + sum(-x for x in numbers[1:]),
        '*': lambda: reduce(lambda a, b: a * b, numbers, 1),
        '/': lambda: divide(numbers),
    }
    return actions[operator]()

# if __name__ == '__main__':
#     operator_input = input()
#     numbers_input = [int(x) for x in input().split()]
#     final_result = operate(operator=operator_input, *numbers_input)
#     print(final_result)
