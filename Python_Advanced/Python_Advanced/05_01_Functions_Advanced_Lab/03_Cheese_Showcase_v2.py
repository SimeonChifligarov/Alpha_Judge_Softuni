def sorting_cheeses(**cheese_data: list[int]) -> str:
    """
    This function sorts cheeses by how many pieces they have and lists their amounts.

    Args:
        **cheese_data (list[int]): Cheese names with their piece quantities.

    Returns:
        str: A nicely formatted list of cheeses and their pieces.
    """
    sorted_cheeses = sorted(
        cheese_data.items(),
        key=lambda item: (-len(item[1]), item[0])
    )
    result = []
    for cheese, pieces in sorted_cheeses:
        result.append(cheese)
        result.extend(str(piece) for piece in sorted(pieces, reverse=True))
    return '\n'.join(result)

# if __name__ == '__main__':
#     cheeses_input = {
#         'Cheddar': [2, 4, 6],
#         'Brie': [5, 3],
#         'Gouda': [1, 2, 3, 4],
#     }
#     output = sorting_cheeses(**cheeses_input)
#     print(output)
