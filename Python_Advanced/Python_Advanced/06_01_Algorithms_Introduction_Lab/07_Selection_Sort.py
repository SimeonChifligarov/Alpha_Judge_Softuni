def selection_sort(numbers: list[int]) -> list[int]:
    """
    Sort the list using selection sort algorithm.

    Args:
        numbers: list of integers to sort

    Returns:
        Sorted list of integers
    """
    for index in range(len(numbers)):
        min_index = index
        for next_index in range(index + 1, len(numbers)):
            if numbers[next_index] < numbers[min_index]:
                min_index = next_index
        numbers[index], numbers[min_index] = numbers[min_index], numbers[index]
    return numbers


if __name__ == '__main__':
    input_numbers = [int(el) for el in input().split()]
    sorted_numbers = selection_sort(numbers=input_numbers)
    print(' '.join(str(el) for el in sorted_numbers))
