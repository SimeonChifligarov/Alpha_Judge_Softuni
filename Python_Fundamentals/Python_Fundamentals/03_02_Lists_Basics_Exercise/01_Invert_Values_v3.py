from typing import List


def get_opposites(numbers: str) -> List[int]:
    """Returns a list containing the opposite of each number in the input string."""

    return [-int(num) for num in numbers.split()]


if __name__ == '__main__':
    input_string = input()
    result = get_opposites(numbers=input_string)
    print(result)
