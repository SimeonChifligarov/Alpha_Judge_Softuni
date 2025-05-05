def iterative_factorial(number: int) -> int:
    """
    Loop to get factorial of a number.

    Args:
        number: input integer

    Returns:
        Factorial of the number
    """
    result = 1
    for current in range(2, number + 1):
        result *= current
    return result


if __name__ == '__main__':
    input_number = int(input())
    result = iterative_factorial(number=input_number)
    print(result)
