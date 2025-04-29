def sorting_cheeses(**entries: list[int]) -> str:
    """
    This function sorts cheeses by quantity and makes a nice output.

    Args:
        **entries (list[int]): Cheese names with their piece numbers.

    Returns:
        str: A string that lists cheeses and their sorted pieces.
    """
    cheeses_sorted = sorted(
        entries.items(),
        key=lambda pair: (-len(pair[1]), pair[0])
    )
    output = []
    for cheese_name, pieces in cheeses_sorted:
        output.append(cheese_name)
        output += [str(quantity) for quantity in sorted(pieces, reverse=True)]
    return '\n'.join(output)

# if __name__ == '__main__':
#     cheese_input = {
#         'Emmental': [7, 2, 5],
#         'Gruyere': [4, 4, 1, 2],
#         'Roquefort': [3, 3],
#     }
#     showcase_result = sorting_cheeses(**cheese_input)
#     print(showcase_result)
