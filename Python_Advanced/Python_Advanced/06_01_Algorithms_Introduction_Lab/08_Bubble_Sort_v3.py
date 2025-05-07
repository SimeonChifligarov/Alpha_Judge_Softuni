def count_calls(func):
    """
    Count calls to a function.
    """

    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        return func(*args, **kwargs)

    wrapper.calls = 0
    return wrapper


@count_calls
def recursive_bubble_sort(numbers: list[int], length: int | None = None) -> list[int]:
    """
    Recursive bubble sort with call counter.

    Args:
        numbers: list of integers
        length: active range

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
    # print(f'Recursive calls: {recursive_bubble_sort.calls}')
