from bisect import bisect_left


def binary_search(numbers: list[int], target: int) -> int:
    """
    Find index using bisect module.

    Args:
        numbers: sorted integers
        target: value to locate

    Returns:
        Index or -1
    """
    index = bisect_left(numbers, target)
    return index if index < len(numbers) and numbers[index] == target else -1


if __name__ == '__main__':
    sorted_numbers = [int(el) for el in input().split()]
    target_value = int(input())
    index_result = binary_search(numbers=sorted_numbers, target=target_value)
    print(index_result)
