def count_calls(func):
    """
    Decorator to count how many times a recursive function was called.
    """

    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        return func(*args, **kwargs)

    wrapper.calls = 0
    return wrapper


@count_calls
def binary_search(numbers: list[int], target: int, start: int = 0, end: int | None = None) -> int:
    """
    Binary search with decorator counting calls.

    Args:
        numbers: sorted list
        target: value to find
        start: start index
        end: end index

    Returns:
        Index or -1
    """
    if end is None:
        end = len(numbers) - 1
    if start > end:
        return -1
    mid = (start + end) // 2
    if numbers[mid] == target:
        return mid
    if numbers[mid] < target:
        return binary_search(numbers=numbers, target=target, start=mid + 1, end=end)
    return binary_search(numbers=numbers, target=target, start=start, end=mid - 1)


if __name__ == '__main__':
    sorted_numbers = [int(el) for el in input().split()]
    target_value = int(input())
    result = binary_search(numbers=sorted_numbers, target=target_value)
    print(result)
    # print(f'Function called {binary_search.calls} time(s)')
