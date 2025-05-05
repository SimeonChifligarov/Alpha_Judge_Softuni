def recursive_factorial(value: int) -> int:
    """
    Return the factorial of a number using recursion.

    Args:
        value: number to calculate factorial

    Returns:
        Factorial result
    """
    return 1 if value in {0, 1} else value * recursive_factorial(value=value - 1)


if __name__ == '__main__':
    input_value = int(input())
    result = recursive_factorial(value=input_value)
    print(result)
