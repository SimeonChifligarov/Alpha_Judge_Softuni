def recursive_power(base: int, exponent: int) -> int:
    """
    This function finds the power of a number by using recursion.

    Args:
        base (int): The number to multiply.
        exponent (int): How many times to multiply the number.

    Returns:
        int: The final result after doing the power.
    """
    if exponent == 0:
        return 1
    return base * recursive_power(base, exponent - 1)

# if __name__ == '__main__':
#     base_input = int(input())
#     exponent_input = int(input())
#     power_result = recursive_power(base=base_input, exponent=exponent_input)
#     print(power_result)
