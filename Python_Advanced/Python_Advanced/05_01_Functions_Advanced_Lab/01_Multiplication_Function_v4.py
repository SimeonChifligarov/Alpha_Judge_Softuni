def multiply(*digits: int) -> int:
    """
    This function finds the multiplication of many numbers that are given.

    Args:
        *digits (int): All the numbers to multiply.

    Returns:
        int: The multiplied answer.
    """
    product = 1
    index = 0
    while index < len(digits):
        product *= digits[index]
        index += 1
    return product

# if __name__ == '__main__':
#     digits_input = [int(x) for x in input().split()]
#     result_value = multiply(*digits_input)
#     print(result_value)
