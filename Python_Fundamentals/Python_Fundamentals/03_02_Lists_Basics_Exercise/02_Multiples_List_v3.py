from typing import List


def generate_multiples(factor: int, count: int) -> List[int]:
    """
    Generates a list of integers that are multiples of the given factor,
    with a length equal to the specified count.
    """
    return [factor * i for i in range(1, count + 1)]


if __name__ == '__main__':
    factor_input = int(input())
    count_input = int(input())
    result = generate_multiples(factor=factor_input, count=count_input)
    print(result)
