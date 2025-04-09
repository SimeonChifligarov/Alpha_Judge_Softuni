from typing import List


def reverse_numbers(numbers: List[int]) -> List[int]:
    """
    Reverses a list of integers using a stack approach and returns the reversed list.
    """
    stack = []
    for number in numbers:
        stack.append(number)
    reversed_list = [stack.pop() for _ in range(len(stack))]
    return reversed_list


if __name__ == '__main__':
    numbers_input = [int(el) for el in input().split()]
    reversed_output = reverse_numbers(numbers=numbers_input)
    print(*reversed_output)
