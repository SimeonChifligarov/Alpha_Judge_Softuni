from functools import reduce


def concatenate(*elements: str, **mapping: str) -> str:
    """
    This function merges words into one and applies replacements from the mapping.

    Args:
        elements: Words to be merged
        mapping: Words to be replaced with other words

    Returns:
        A string after merging and applying changes
    """
    joined = reduce(lambda x, y: x + y, elements)
    final = reduce(lambda text, pair: text.replace(pair[0], pair[1]), mapping.items(), joined)
    return final

# if __name__ == '__main__':
#     input_mapping = {
#         'Hello': 'Hi',
#         'World': 'Earth'
#     }
#     print(concatenate('Hello', 'World', **input_mapping))
