from typing import List


def reverse_numbers_stack(values: List[int]) -> List[int]:
    """
    Reverses a list of integers using a deque as a stack and returns the reversed list.
    """
    reversed_result = [values.pop() for _ in range(len(values))]
    return reversed_result


if __name__ == '__main__':
    values_input = [int(el) for el in input().split()]
    reversed_values_output = reverse_numbers_stack(values=values_input)
    print(*reversed_values_output)
