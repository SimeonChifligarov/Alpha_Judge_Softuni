def selection_sort(numbers: list[int]) -> list[int]:
    """
    Perform selection sort on a list.

    Args:
        numbers: list of integers

    Returns:
        Sorted list
    """
    for i in range(len(numbers)):
        min_i = min(range(i, len(numbers)), key=lambda j: numbers[j])
        numbers[i], numbers[min_i] = numbers[min_i], numbers[i]
    return numbers


if __name__ == '__main__':
    input_numbers = [int(el) for el in input().split()]
    sorted_numbers = selection_sort(numbers=input_numbers)
    print(' '.join(str(el) for el in sorted_numbers))
