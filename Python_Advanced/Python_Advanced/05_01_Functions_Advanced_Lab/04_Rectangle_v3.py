def rectangle(side_1: int, side_2: int) -> str:
    """
    This function returns the area and perimeter of a rectangle if the values are valid.

    Args:
        side_1 (int): The first side of the rectangle.
        side_2 (int): The second side of the rectangle.

    Returns:
        str: A string showing the area and perimeter or a warning message.
    """
    if type(side_1) is not int or type(side_2) is not int:
        return 'Enter valid values!'

    def calculate_area() -> int:
        """
        This function finds the area from two sides.

        Returns:
            int: The result of the area.
        """
        return side_1 * side_2

    def calculate_perimeter() -> int:
        """
        This function finds the perimeter from two sides.

        Returns:
            int: The result of the perimeter.
        """
        return 2 * (side_1 + side_2)

    return f'Rectangle area: {calculate_area()}\nRectangle perimeter: {calculate_perimeter()}'

# if __name__ == '__main__':
#     side_1_input = int(input())
#     side_2_input = int(input())
#     result_output = rectangle(side_1=side_1_input, side_2=side_2_input)
#     print(result_output)
