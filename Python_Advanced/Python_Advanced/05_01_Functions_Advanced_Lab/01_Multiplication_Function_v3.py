def multiply(*values: int) -> int:
    """
    This function takes many numbers and multiplies them into one answer.

    Args:
        *values (int): Many integers to multiply together.

    Returns:
        int: The final multiplied number.
    """
    # TODO: do not use this one ;)
    return eval('*'.join(str(v) for v in values)) if values else 0

# if __name__ == '__main__':
#     input_values = [int(el) for el in input().split()]
#     output_result = multiply(*input_values)
#     print(output_result)
