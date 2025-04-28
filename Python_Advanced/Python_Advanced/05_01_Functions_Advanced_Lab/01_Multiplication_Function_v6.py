from functools import reduce


def multiply(*items: int) -> int:
    """
    This function multiplies all numbers that are given into one result.

    Args:
        *items (int): All integers to multiply together.

    Returns:
        int: The final multiplied value.
    """
    return reduce(lambda x, y: x * y, items, 1)

# if __name__ == '__main__':
#     numbers_input = [int(el) for el in input().split()]
#     multiplication_result = multiply(*numbers_input)
#     print(multiplication_result)
