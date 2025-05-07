def insertion_sort(numbers: list[int]) -> list[int]:
    """
    Sort the list using the insertion sort algorithm.

    Args:
        numbers: list of integers to sort

    Returns:
        Sorted list of integers
    """
    for index in range(1, len(numbers)):
        current = numbers[index]
        position = index - 1
        while position >= 0 and numbers[position] > current:
            numbers[position + 1] = numbers[position]
            position -= 1
        numbers[position + 1] = current
    return numbers


if __name__ == '__main__':
    input_numbers = [int(el) for el in input().split()]
    sorted_numbers = insertion_sort(numbers=input_numbers)
    print(' '.join(str(el) for el in sorted_numbers))
