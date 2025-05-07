def count_calls(func):
    """
    Count how many times the recursive function is called.
    """

    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        return func(*args, **kwargs)

    wrapper.calls = 0
    return wrapper


@count_calls
def recursive_insertion_sort(numbers: list[int], index: int = 1) -> list[int]:
    """
    Sort the list using recursive insertion sort.

    Args:
        numbers: list of integers to sort
        index: current index being inserted

    Returns:
        Sorted list
    """
    if index == len(numbers):
        return numbers

    current = numbers[index]
    position = index - 1

    while position >= 0 and numbers[position] > current:
        numbers[position + 1] = numbers[position]
        position -= 1

    numbers[position + 1] = current
    return recursive_insertion_sort(numbers=numbers, index=index + 1)


if __name__ == '__main__':
    input_numbers = [int(el) for el in input().split()]
    sorted_numbers = recursive_insertion_sort(numbers=input_numbers)
    print(' '.join(str(el) for el in sorted_numbers))
    # print(f'Recursive calls: {recursive_insertion_sort.calls}')
