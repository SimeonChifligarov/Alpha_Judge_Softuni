def age_assignment(*names: str, **letters: int) -> str:
    """
    This function assigns ages to names based on their first letter.

    Args:
        names: People names
        letters: Mapping of first letters to ages

    Returns:
        A string with names and their assigned ages
    """
    assigned = [f'{name} is {letters[name[0]]} years old.' for name in sorted(names)]
    return '\n'.join(assigned)

# if __name__ == '__main__':
#     result = age_assignment(
#         'Alice', 'Bob', 'Charlie',
#         A=25,
#         B=30,
#         C=20
#     )
#     print(result)
