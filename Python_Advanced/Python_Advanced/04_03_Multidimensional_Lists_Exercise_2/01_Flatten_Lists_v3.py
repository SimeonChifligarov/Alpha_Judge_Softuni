def flatten_and_reverse(input_string: str) -> list[int]:
    """
    This function flattens and reverses a list of numbers separated by pipes and spaces.

    Args:
    input_string: a string with sublists split by '|', and numbers split by spaces

    Returns:
    A single flattened list of integers in reversed sublist order
    """
    return [int(x) for part in input_string.split('|')[::-1] for x in part.split() if x]


if __name__ == '__main__':
    raw_input = input()
    final_list = flatten_and_reverse(input_string=raw_input)
    print(*final_list)
