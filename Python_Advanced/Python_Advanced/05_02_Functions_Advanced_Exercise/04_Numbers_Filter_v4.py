def even_odd_filter(**collections: list[int]) -> dict[str, list[int]]:
    """
    This function filters numbers into even or odd based on the key name.

    Args:
        collections: Named lists with 'even' or 'odd' as keys

    Returns:
        A dictionary with filtered lists, sorted by their size from biggest to smallest
    """
    filtered_collections = {}
    operations = {
        'even': lambda x: x % 2 == 0,
        'odd': lambda x: x % 2 != 0,
    }
    for category, numbers in collections.items():
        filtered_collections[category] = [number for number in numbers if operations[category](number)]
    return dict(sorted(filtered_collections.items(), key=lambda item: len(item[1]), reverse=True))

# if __name__ == '__main__':
#     given_collections = {
#         'odd': [10, 11, 12, 13],
#         'even': [2, 4, 6, 8, 10]
#     }
#     print(even_odd_filter(**given_collections))
