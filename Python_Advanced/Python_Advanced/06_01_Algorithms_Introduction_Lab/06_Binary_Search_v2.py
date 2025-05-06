def binary_search(numbers: list[int], target: int) -> int:
    """
    Find the index of a number using binary search in a sorted list.

    Args:
        numbers: sorted list of integers
        target: the value to search for

    Returns:
        The index of the target value, or -1 if not found
    """
    start = 0
    end = len(numbers) - 1

    while start <= end:
        middle = (start + end) // 2
        if numbers[middle] == target:
            return middle
        elif numbers[middle] < target:
            start = middle + 1
        else:
            end = middle - 1

    return -1


if __name__ == '__main__':
    sorted_numbers = [int(el) for el in input().split()]
    target_value = int(input())
    index = binary_search(numbers=sorted_numbers, target=target_value)
    print(index)
