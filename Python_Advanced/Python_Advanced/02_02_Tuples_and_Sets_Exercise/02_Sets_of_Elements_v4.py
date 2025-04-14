def find_same_numbers(first_length: int, second_length: int) -> set:
    """
    This function finds numbers that are common in two sets.

    Args:
        first_length (int): How many numbers for first set
        second_length (int): How many numbers for second set

    Returns:
        set: Set with numbers that are common in both
    """
    first_group = set()
    second_group = set()
    for _ in range(first_length):
        first_group.add(input())
    for _ in range(second_length):
        second_group.add(input())
    same_numbers = first_group.intersection(second_group)
    return same_numbers


if __name__ == '__main__':
    length_inputs = [int(el) for el in input().split()]
    first_input_length = length_inputs[0]
    second_input_length = length_inputs[1]
    repeated_numbers = find_same_numbers(first_length=first_input_length, second_length=second_input_length)
    print('\n'.join(repeated_numbers))
