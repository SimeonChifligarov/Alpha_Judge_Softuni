def multiply(*elements: int) -> int:
    """
    This function multiplies many numbers into one final number.

    Args:
        *elements (int): Many integers that need to be multiplied.

    Returns:
        int: The multiplication result.
    """
    if not elements:
        return 0
    if len(elements) == 1:
        return elements[0]
    first = elements[0]
    rest = multiply(*elements[1:])
    return first * rest

# if __name__ == '__main__':
#     elements_input = [int(number) for number in input().split()]
#     final_result = multiply(*elements_input)
#     print(final_result)
