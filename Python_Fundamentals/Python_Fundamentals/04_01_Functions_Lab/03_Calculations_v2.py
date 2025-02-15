def calculate_result(operator: str, num_1: int, num_2: int) -> int:
    """
    Performs a mathematical operation based on the given operator.
    If operator is not valid return 0.
    """
    result = 0
    if operator == 'multiply':
        result = num_1 * num_2
    elif operator == 'divide':
        result = num_1 // num_2
    elif operator == 'add':
        result = num_1 + num_2
    elif operator == 'subtract':
        result = num_1 - num_2
    return result


if __name__ == '__main__':
    op = input()
    val_1 = int(input())
    val_2 = int(input())
    output = calculate_result(operator=op, num_1=val_1, num_2=val_2)
    print(output)
