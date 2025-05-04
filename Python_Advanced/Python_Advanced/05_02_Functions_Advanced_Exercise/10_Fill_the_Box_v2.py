def fill_the_box(height: int, length: int, width: int, *elements: int) -> str:
    """
    This function fills a box with cubes and checks if there is space or overflow.

    Args:
        height: Height of the box
        length: Length of the box
        width: Width of the box
        elements: Cubes numbers and the string 'Finish'

    Returns:
        A message if space is left or cubes are left
    """
    capacity = height * length * width
    index = 0
    total_cubes = 0
    while index < len(elements):
        current = elements[index]
        if current == 'Finish':
            break
        total_cubes += current
        index += 1
    if total_cubes <= capacity:
        return f'There is free space in the box. You could put {capacity - total_cubes} more cubes.'
    return f'No more free space! You have {total_cubes - capacity} more cubes.'


if __name__ == '__main__':
    input_elements = (5, 5, 2, 40, 11, 7, 3, 1, 5, 'Finish')
    print(fill_the_box(*input_elements))
