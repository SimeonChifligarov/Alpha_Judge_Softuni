def calculate_rectangle_area(width: int, height: int) -> int:
    """
    Calculates the area of a rectangle given its width and height.
    """
    result = width * height
    return result


if __name__ == '__main__':
    width_input = int(input())
    height_input = int(input())
    area = calculate_rectangle_area(width=width_input, height=height_input)
    print(area)
