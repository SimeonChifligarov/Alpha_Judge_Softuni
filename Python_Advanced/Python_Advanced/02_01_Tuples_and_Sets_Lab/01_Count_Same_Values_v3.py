def count_numbers_occurrences(numbers_list: list[float]) -> None:
    """
    Count how many times each number appears and print it.

    Args:
        numbers_list (list[float]): List of numbers.

    Returns:
        None
    """
    numbers_tuple = tuple(round(el, 1) for el in numbers_list)
    unique_numbers = []
    for element in numbers_tuple:
        if element not in unique_numbers:
            unique_numbers.append(element)
    for number in unique_numbers:
        print(f'{number:.1f} - {numbers_tuple.count(number)} times')


if __name__ == '__main__':
    numbers_input = [float(el) for el in input().split()]
    count_numbers_occurrences(numbers_list=numbers_input)
