def even_odd_filter(**data: list[int]) -> dict[str, list[int]]:
    """
    This function takes named lists of numbers and filters them by even or odd.

    Args:
        data: Keyword arguments with 'even' or 'odd' keys and list of numbers as values

    Returns:
        A dictionary with filtered lists, sorted by list length descending
    """
    filtered = {
        key: [value for value in values if value % 2 == 0] if key == 'even' else [value for value in values if
                                                                                  value % 2 != 0]
        for key, values in data.items()
    }
    sorted_filtered = dict(sorted(filtered.items(), key=lambda x: len(x[1]), reverse=True))
    return sorted_filtered

# if __name__ == '__main__':
#     result = even_odd_filter(
#         even=[1, 2, 3, 4, 5, 6],
#         odd=[1, 3, 5, 7, 9],
#     )
#     print(result)
