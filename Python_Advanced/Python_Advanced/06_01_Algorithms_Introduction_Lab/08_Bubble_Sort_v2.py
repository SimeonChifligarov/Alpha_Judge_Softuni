def recursive_bubble_sort(numbers: list[int], length: int | None = None) -> list[int]:
    """
    Recursively sort a list using bubble sort.

    Args:
        numbers: list of integers
        length: current pass length

    Returns:
        Sorted list
    """
    length = len(numbers) if length is None else length
    if length == 1:
        return numbers
    for i in range(length - 1):
        if numbers[i] > numbers[i + 1]:
            numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
    return recursive_bubble_sort(numbers=numbers, length=length - 1)


if __name__ == '__main__':
    input_numbers = [int(el) for el in input().split()]
    sorted_numbers = recursive_bubble_sort(numbers=input_numbers)
    print(' '.join(str(el) for el in sorted_numbers))
