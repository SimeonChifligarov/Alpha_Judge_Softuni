def even_odd(*entries: int) -> list[int]:
    """
    This function takes many numbers and a command, and gives back a filtered list.

    Args:
        entries: Several integers and at the end a command 'even' or 'odd'

    Returns:
        A list with numbers filtered by the command
    """
    command = entries[-1]
    values = entries[:-1]
    filter_function = (lambda x: x % 2 == 0) if command == 'even' else (lambda x: x % 2 != 0)
    return [value for value in values if filter_function(value)]

# if __name__ == '__main__':
#     input_entries = [int(item) if item.lstrip('-').isdigit() else item for item in input().split()]
#     print(even_odd(*input_entries))
