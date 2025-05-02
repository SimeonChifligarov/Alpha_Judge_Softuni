def concatenate(*words: str, **replacements: str) -> str:
    """
    This function puts together words and then replaces parts based on given replacements.

    Args:
        words: Many words to join
        replacements: Named pairs where the key will be replaced by the value

    Returns:
        A final string after joining and replacing
    """
    result = ''.join(words)
    for target, replacement in replacements.items():
        if target in result:
            result = result.replace(target, replacement)
    return result

# if __name__ == '__main__':
#     final_result = concatenate(
#         'I', 'Love', 'Python',
#         Love='Enjoy',
#         Python='Coding',
#     )
#     print(final_result)
