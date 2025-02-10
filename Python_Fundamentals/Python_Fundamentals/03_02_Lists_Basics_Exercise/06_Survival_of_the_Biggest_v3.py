from typing import List


def remove_smallest_numbers(numbers: List[int], count: int) -> List[int]:
    """
    Removes the smallest `count` numbers from the list and returns the remaining numbers.
    """

    for _ in range(count):
        numbers.remove(min(numbers))

    return numbers


if __name__ == '__main__':
    numbers_input = [int(n) for n in input().split()]
    count_input = int(input())
    remaining_numbers = remove_smallest_numbers(numbers=numbers_input, count=count_input)
    print(', '.join(map(str, remaining_numbers)))
