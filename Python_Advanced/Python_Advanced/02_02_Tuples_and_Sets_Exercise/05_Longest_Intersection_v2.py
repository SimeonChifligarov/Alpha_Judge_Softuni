def find_longest_intersection(ranges_count: int) -> tuple:
    """
    This function finds the longest intersection from given ranges.

    Args:
        ranges_count (int): How many range pairs to check

    Returns:
        tuple: The longest intersection and its length
    """
    longest_part = set()
    for _ in range(ranges_count):
        ranges_input = input().split('-')
        first_range = [int(el) for el in ranges_input[0].split(',')]
        second_range = [int(el) for el in ranges_input[1].split(',')]
        first_set = {num for num in range(first_range[0], first_range[1] + 1)}
        second_set = {num for num in range(second_range[0], second_range[1] + 1)}
        current_intersection = first_set.intersection(second_set)
        if len(current_intersection) > len(longest_part):
            longest_part = current_intersection
    return list(longest_part), len(longest_part)


if __name__ == '__main__':
    total_ranges = int(input())
    longest_result, result_length = find_longest_intersection(ranges_count=total_ranges)
    print(f'Longest intersection is [{", ".join(str(num) for num in longest_result)}] with length {result_length}')
