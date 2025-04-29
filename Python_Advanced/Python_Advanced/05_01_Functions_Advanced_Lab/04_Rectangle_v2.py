def rectangle(length: int, width: int) -> str:
    """
    This function checks if values are valid and returns the area and perimeter of a rectangle.

    Args:
        length (int): The length of the rectangle.
        width (int): The width of the rectangle.

    Returns:
        str: The area and perimeter in a simple format or a message for invalid input.
    """
    if not isinstance(length, int) or not isinstance(width, int):
        return 'Enter valid values!'

    def area() -> int:
        """
        This function calculates the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return length * width

    def perimeter() -> int:
        """
        This function calculates the perimeter of the rectangle.

        Returns:
            int: The perimeter of the rectangle.
        """
        return 2 * (length + width)

    return f'Rectangle area: {area()}\nRectangle perimeter: {perimeter()}'

# if __name__ == '__main__':
#     length_input = int(input())
#     width_input = int(input())
#     rectangle_result = rectangle(length=length_input, width=width_input)
#     print(rectangle_result)
