def multiply(*numbers: int) -> int:
    """
    This function multiplies all given numbers together.

    Args:
        *numbers (int): Any amount of integers to multiply.

    Returns:
        int: The result of the multiplication.
    """
    result = 1
    for number in numbers:
        result *= number
    return result

# if __name__ == '__main__':
#     values_input = [int(x) for x in input().split()]
#     result_output = multiply(*values_input)
#     print(result_output)
