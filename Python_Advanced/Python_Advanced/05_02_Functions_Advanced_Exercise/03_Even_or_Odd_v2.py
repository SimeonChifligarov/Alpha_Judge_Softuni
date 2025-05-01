def even_odd(*values: int) -> list[int]:
    """
    This function takes numbers and a command, then returns only even or odd numbers.

    Args:
        values: A bunch of numbers with the last one being 'even' or 'odd'

    Returns:
        A list with filtered numbers
    """
    command = values[-1]
    numbers = values[:-1]
    if command == 'even':
        return [n for n in numbers if n % 2 == 0]
    return [n for n in numbers if n % 2 != 0]

# if __name__ == '__main__':
#     given_items = [int(value) if value.lstrip('-').isdigit() else value for value in input().split()]
#     print(even_odd(*given_items))
