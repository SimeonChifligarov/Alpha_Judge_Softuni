def find_sign(num_1: int, num_2: int, num_3: int) -> str:
    """
    Determines whether the product of three numbers is negative, positive, or zero without multiplying them.

    :param num_1: The first integer.
    :param num_2: The second integer.
    :param num_3: The third integer.
    :return: A string indicating whether the product is "negative", "positive", or "zero".
    """
    if 0 in (num_1, num_2, num_3):
        return 'zero'

    negative_count = sum(1 for num in (num_1, num_2, num_3) if num < 0)

    return 'negative' if negative_count % 2 == 1 else 'positive'


if __name__ == '__main__':
    num_1_input = int(input())
    num_2_input = int(input())
    num_3_input = int(input())

    result = find_sign(num_1=num_1_input, num_2=num_2_input, num_3=num_3_input)
    print(result)
