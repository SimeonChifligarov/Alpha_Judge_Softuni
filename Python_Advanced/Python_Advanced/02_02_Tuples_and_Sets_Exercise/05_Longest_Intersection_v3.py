def get_largest_intersection(number_of_lines: int) -> tuple:
    """
    This function gets the largest intersection between given ranges.

    Args:
        number_of_lines (int): The number of input lines

    Returns:
        tuple: A list with the intersection numbers and the size of the intersection
    """
    intersections = []
    for _ in range(number_of_lines):
        first_part, second_part = input().split('-')
        first_start, first_end = [int(x) for x in first_part.split(',')]
        second_start, second_end = [int(x) for x in second_part.split(',')]
        first_range = set(range(first_start, first_end + 1))
        second_range = set(range(second_start, second_end + 1))
        intersections.append(first_range & second_range)
    best_intersection = max(intersections, key=lambda s: len(s))
    return list(best_intersection), len(best_intersection)


if __name__ == '__main__':
    lines_count_input = int(input())
    final_intersection, intersection_length = get_largest_intersection(number_of_lines=lines_count_input)
    print(
        f'Longest intersection is [{", ".join(str(n) for n in final_intersection)}] with length {intersection_length}'
    )
