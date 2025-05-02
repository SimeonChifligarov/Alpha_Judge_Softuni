def even_odd_filter(**numbers: list[int]) -> dict[str, list[int]]:
    """
    This function gets lists of numbers and keeps only even or odd numbers as needed.

    Args:
        numbers: Keyword arguments where keys are 'even' or 'odd' and values are lists of numbers

    Returns:
        A dictionary with filtered numbers, sorted by size of lists in descending order
    """
    result = {}
    for kind, values in numbers.items():
        if kind == 'even':
            result[kind] = [num for num in values if num % 2 == 0]
        if kind == 'odd':
            result[kind] = [num for num in values if num % 2 != 0]
    sorted_result = dict(sorted(result.items(), key=lambda pair: -len(pair[1])))
    return sorted_result

# if __name__ == '__main__':
#     input_numbers = {
#         'even': [2, 4, 6, 7, 9],
#         'odd': [1, 3, 5, 8]
#     }
#     print(even_odd_filter(**input_numbers))
