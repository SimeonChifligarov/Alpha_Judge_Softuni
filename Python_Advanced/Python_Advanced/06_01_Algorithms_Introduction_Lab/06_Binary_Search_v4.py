def recursive_binary_search(numbers: list[int], target: int, start: int, end: int) -> int:
    """
    Recursively search for value in sorted list.

    Args:
        numbers: list of sorted integers
        target: number to find
        start: search start index
        end: search end index

    Returns:
        Index or -1
    """
    if start > end:
        return -1
    mid = (start + end) // 2
    if numbers[mid] == target:
        return mid
    return (
        recursive_binary_search(numbers=numbers, target=target, start=mid + 1, end=end) if numbers[mid] < target
        else recursive_binary_search(numbers=numbers, target=target, start=start, end=mid - 1)
    )


if __name__ == '__main__':
    sorted_numbers = [int(el) for el in input().split()]
    target_value = int(input())
    index = recursive_binary_search(numbers=sorted_numbers, target=target_value, start=0, end=len(sorted_numbers) - 1)
    print(index)
