def even_odd(*items: int) -> list[int]:
    """
    This function gets numbers and a command, and filters based on the command.

    Args:
        items: Many integers with the last one being 'even' or 'odd'

    Returns:
        A list with only even or only odd numbers
    """
    command = items[-1]
    numbers = items[:-1]
    return (
        [number for number in numbers if number % 2 == 0] if command == 'even'
        else [number for number in numbers if number % 2 != 0]
    )

# if __name__ == '__main__':
#     given_items = [int(value) if value.lstrip('-').isdigit() else value for value in input().split()]
#     print(even_odd(*given_items))
