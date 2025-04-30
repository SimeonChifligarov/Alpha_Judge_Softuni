def recursive_power(value: int, power: int) -> int:
    """
    This function calculates a number raised to a power using recursion.

    Args:
        value (int): The number to be powered.
        power (int): The number of times to multiply.

    Returns:
        int: The result after raising the number to the power.
    """
    return 1 if power == 0 else value * recursive_power(value=value, power=power - 1)

# if __name__ == '__main__':
#     value_input = int(input())
#     power_input = int(input())
#     result = recursive_power(value=value_input, power=power_input)
#     print(result)
