def fill_the_box(height: int, length: int, width: int, *quantities: int) -> str:
    """
    This function puts cubes inside a box and tells if space was enough.

    Args:
        height: Height of the box
        length: Length of the box
        width: Width of the box
        quantities: A lot of cubes and then 'Finish' string

    Returns:
        A string showing if there is free space or cubes left
    """
    volume = height * length * width
    total_cubes = 0
    for quantity in quantities:
        if quantity == 'Finish':
            break
        total_cubes += quantity
    if total_cubes <= volume:
        return f'There is free space in the box. You could put {volume - total_cubes} more cubes.'
    return f'No more free space! You have {total_cubes - volume} more cubes.'


if __name__ == '__main__':
    result = fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, 'Finish')
    print(result)
