def evaluate_expression(expression_parts: list[str]) -> int:
    """
    This function solves a math expression from left to right when meeting an operator.

    Args:
        expression_parts (list[str]): A list with numbers and operators.

    Returns:
        int: The final result after evaluation.
    """
    numbers = []
    for part in expression_parts:
        if part in {'*', '+', '-', '/'}:
            result = numbers[0]
            for number in numbers[1:]:
                if part == '*':
                    result *= number
                elif part == '+':
                    result += number
                elif part == '-':
                    result -= number
                elif part == '/':
                    result //= number
            numbers = [result]
        else:
            numbers.append(int(part))
    return numbers[0]


if __name__ == '__main__':
    expression_input = input().split()
    result = evaluate_expression(expression_parts=expression_input)
    print(result)
