def recursive_factorial(value: int) -> int:
    """
    Get the factorial of a number using recursion.

    Args:
        value: the number to compute factorial for

    Returns:
        The factorial of the number
    """
    if value == 0 or value == 1:
        return 1
    return value * recursive_factorial(value=value - 1)


if __name__ == '__main__':
    input_value = int(input())
    result = recursive_factorial(value=input_value)
    print(result)
