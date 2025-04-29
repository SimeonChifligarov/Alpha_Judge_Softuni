def sorting_cheeses(**cheeses: list[int]) -> str:
    """
    This function arranges cheeses by their piece counts and shows them nicely.

    Args:
        **cheeses (list[int]): The cheeses and their piece quantities.

    Returns:
        str: A formatted string of cheeses and their sorted pieces.
    """
    ordered = sorted(
        [(name, sorted(amounts, reverse=True)) for name, amounts in cheeses.items()],
        key=lambda x: (-len(x[1]), x[0])
    )
    lines = [name + '\n' + '\n'.join(str(p) for p in pieces) for name, pieces in ordered]
    return '\n'.join(lines)

# if __name__ == '__main__':
#     cheeses_data = {
#         'Parmesan': [2, 1],
#         'Mozzarella': [5, 4, 6],
#         'Camembert': [1, 1, 1],
#     }
#     final_result = sorting_cheeses(**cheeses_data)
#     print(final_result)
