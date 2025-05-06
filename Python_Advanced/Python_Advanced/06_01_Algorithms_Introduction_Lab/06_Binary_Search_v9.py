def binary_search_tail(numbers: list[int], target: int) -> int:
    """
    Tail-recursive style binary search using iteration to avoid recursion.

    Args:
        numbers: sorted integers
        target: value to find

    Returns:
        Index of target or -1
    """
    start = 0
    end = len(numbers) - 1

    def loop(start_index: int, end_index: int) -> int:
        while start_index <= end_index:
            mid = (start_index + end_index) // 2
            if numbers[mid] == target:
                return mid
            if numbers[mid] < target:
                start_index = mid + 1
            else:
                end_index = mid - 1
        return -1

    return loop(start_index=start, end_index=end)


if __name__ == '__main__':
    sorted_numbers = [int(el) for el in input().split()]
    target_value = int(input())
    index = binary_search_tail(numbers=sorted_numbers, target=target_value)
    print(index)
