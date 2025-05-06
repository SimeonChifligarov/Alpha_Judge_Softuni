def binary_search_enum(pairs: list[int], target: int) -> int:
    """
    Binary search using (index, value) pairs.

    Args:
        pairs: list of (index, value) from enumerate
        target: number to find

    Returns:
        Index of the target or -1
    """
    left = 0
    right = len(pairs) - 1

    while left <= right:
        mid = (left + right) // 2
        _, value = pairs[mid]
        if value == target:
            return pairs[mid][0]
        elif value < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


if __name__ == '__main__':
    sorted_numbers = [int(el) for el in input().split()]
    target_value = int(input())
    indexed_pairs = list(enumerate(sorted_numbers))
    result = binary_search_enum(pairs=indexed_pairs, target=target_value)
    print(result)
