def concatenate(*pieces: str, **substitutions: str) -> str:
    """
    This function joins strings and changes parts according to given substitutions.

    Args:
        pieces: Many strings to put together
        substitutions: Keyword pairs where the key will be replaced by the value

    Returns:
        The final changed string
    """
    combined = ''.join([piece for piece in pieces])
    updated = ''.join(
        [substitutions.get(char, char) if any(char in key for key in substitutions) else char for char in combined])
    for old, new in substitutions.items():
        if old in updated:
            updated = updated.replace(old, new)
    return updated

# if __name__ == '__main__':
#     inputs = {
#         'I': 'We',
#         'Programming': 'Coding'
#     }
#     print(concatenate('I', 'Love', 'Programming', **inputs))
