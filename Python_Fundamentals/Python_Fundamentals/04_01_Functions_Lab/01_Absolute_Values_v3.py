# from typing import List


# def absolute_values(numbers: str) -> List[float]:
def absolute_values(numbers: str) -> list[float]:
    """
    Returns a list of absolute values of the given sequence of numbers.

    :param numbers: A string containing numbers separated by a single space.
    :return: A list of absolute values of the given numbers.
    """

    return [abs(float(num)) for num in numbers.split()]


if __name__ == '__main__':
    sequence = input()
    result = absolute_values(numbers=sequence)
    print(result)
