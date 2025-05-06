def binary_search(numbers: list[int], target: int) -> int:
    """
    Return index of target in sorted list using binary search.

    Args:
        numbers: sorted integers
        target: number to find

    Returns:
        Index or -1
    """
    left, right = 0, len(numbers) - 1
    while left <= right:
        mid = (left + right) // 2
        if numbers[mid] == target:
            return mid
        if numbers[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


if __name__ == '__main__':
    sorted_numbers = [int(el) for el in input().split()]
    target_value = int(input())
    index = binary_search(numbers=sorted_numbers, target=target_value)
    print(index)
