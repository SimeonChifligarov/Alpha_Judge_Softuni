from typing import List


def get_absolute_values(numbers: List[float]) -> List[float]:
    """
    Takes a list of integers and returns a list of their absolute values.
    """

    return [abs(number) for number in numbers]


if __name__ == '__main__':
    # numbers_input = list(map(float, input().split()))
    numbers_input = [float(n) for n in input().split()]
    result = get_absolute_values(numbers=numbers_input)
    print(result)
