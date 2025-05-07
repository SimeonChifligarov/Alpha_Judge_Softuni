def insertion_sort(numbers: list[int]) -> list[int]:
    """
    Perform insertion sort on the list.

    Args:
        numbers: list of integers

    Returns:
        Sorted list
    """
    for i in range(1, len(numbers)):
        value = numbers[i]
        j = i - 1
        while j >= 0 and numbers[j] > value:
            numbers[j + 1] = numbers[j]
            j -= 1
        numbers[j + 1] = value
    return numbers


if __name__ == '__main__':
    input_numbers = [int(el) for el in input().split()]
    sorted_numbers = insertion_sort(numbers=input_numbers)
    print(' '.join(str(el) for el in sorted_numbers))
