class Point:
    """
    This class is for a 2D point. It keeps track of x and y coordinates.

    Args:
        x (float): The x position
        y (float): The y position
    """

    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def set_x(self, new_x: float) -> None:
        """
        This method sets a new value for x.

        Args:
            new_x (float): The new x value
        """
        self.x = new_x

    def set_y(self, new_y: float) -> None:
        """
        This method sets a new value for y.

        Args:
            new_y (float): The new y value
        """
        self.y = new_y

    def __str__(self) -> str:
        return f'The point has coordinates ({self.x},{self.y})'

# if __name__ == '__main__':
#     x_val = 3.0
#     y_val = 4.5
#     point_instance = Point(x=x_val, y=y_val)
#     print(str(point_instance))
#     point_instance.set_x(new_x=7.0)
#     point_instance.set_y(new_y=8.5)
#     print(str(point_instance))
