def get_info(name: str, age: int, town: str) -> str:
    """
    This function creates a small sentence about a person using name, age and hometown.

    Args:
        name (str): Name of the person.
        age (int): Age of the person.
        town (str): Town of the person.

    Returns:
        str: A simple sentence describing the person.
    """
    return ' '.join([
        'This is', name,
        'from', town,
        'and he is', f'{age}', 'years old'
    ])

# if __name__ == '__main__':
#     info_input = {
#         'name': input(),
#         'age': int(input()),
#         'town': input(),
#     }
#     final_info = get_info(**info_input)
#     print(final_info)
