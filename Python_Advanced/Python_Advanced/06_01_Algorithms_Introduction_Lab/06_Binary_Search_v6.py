def binary_search(numbers: list[int], target: int, start: int = 0, end: int | None = None) -> int:
    """
    Binary search for a number in sorted list.

    Args:
        numbers: sorted list of integers
        target: number to find
        start: left index of range
        end: right index of range (optional)

    Returns:
        Index of target or -1
    """
    end = len(numbers) - 1 if end is None else end
    if start > end:
        return -1
    mid = (start + end) // 2
    return (
        mid if numbers[mid] == target else binary_search(numbers=numbers, target=target, start=mid + 1, end=end)
        if numbers[mid] < target
        else binary_search(numbers=numbers, target=target, start=start, end=mid - 1)
    )


if __name__ == '__main__':
    sorted_numbers = [int(el) for el in input().split()]
    target_value = int(input())
    index = binary_search(numbers=sorted_numbers, target=target_value)
    print(index)
