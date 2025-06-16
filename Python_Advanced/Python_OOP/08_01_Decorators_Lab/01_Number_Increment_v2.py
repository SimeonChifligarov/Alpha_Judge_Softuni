from typing import Callable


def number_increment(numbers: list[int]) -> list[int]:
    """
    This function increases every number in the list by 1.
    Args:
        numbers (list[int]): list of integers
    Returns:
        list[int]: new list with increased numbers
    """

    def increase() -> list[int]:
        return [element + 1 for element in numbers]

    return increase()

# if __name__ == '__main__':
#     output = number_increment(numbers=[1, 2, 3])
#     print(output)
#     pass
