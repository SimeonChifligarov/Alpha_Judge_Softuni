def recursive_selection_sort(numbers: list[int], start: int = 0) -> list[int]:
    """
    Recursively apply selection sort.

    Args:
        numbers: list of integers
        start: current index

    Returns:
        Sorted list
    """
    if start >= len(numbers) - 1:
        return numbers
    min_i = min(range(start, len(numbers)), key=lambda i: numbers[i])
    numbers[start], numbers[min_i] = numbers[min_i], numbers[start]
    return recursive_selection_sort(numbers=numbers, start=start + 1)


if __name__ == '__main__':
    input_numbers = [int(el) for el in input().split()]
    sorted_numbers = recursive_selection_sort(numbers=input_numbers)
    print(' '.join(str(el) for el in sorted_numbers))
