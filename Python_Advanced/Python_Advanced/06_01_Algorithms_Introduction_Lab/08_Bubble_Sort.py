def bubble_sort(numbers: list[int]) -> list[int]:
    """
    Sort the list using the bubble sort algorithm.

    Args:
        numbers: list of integers to sort

    Returns:
        Sorted list of integers
    """
    n = len(numbers)
    for i in range(n):
        for j in range(0, n - 1 - i):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    return numbers


if __name__ == '__main__':
    input_numbers = [int(el) for el in input().split()]
    sorted_numbers = bubble_sort(numbers=input_numbers)
    print(' '.join(str(el) for el in sorted_numbers))
