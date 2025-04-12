def count_numbers_occurrences(numbers_list: list[float]) -> None:
    """
    Count how many times each number appears and print it.

    Args:
        numbers_list (list[float]): List of numbers.

    Returns:
        None
    """
    numbers_count = {}
    for number in numbers_list:
        number_rounded = round(number, 1)
        numbers_count[number_rounded] = numbers_count.get(number_rounded, 0) + 1
    for number_key in sorted(numbers_count.keys(), key=lambda x: numbers_list.index(x)):
        print(f'{number_key:.1f} - {numbers_count[number_key]} times')


if __name__ == '__main__':
    numbers_input = [float(el) for el in input().split()]
    count_numbers_occurrences(numbers_list=numbers_input)
