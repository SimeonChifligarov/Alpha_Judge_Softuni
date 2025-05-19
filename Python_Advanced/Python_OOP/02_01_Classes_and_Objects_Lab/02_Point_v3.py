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

    def __repr__(self) -> str:
        return f'Point(x={self.x!r}, y={self.y!r})'

    # def __repr__(self) -> str:
    #     cls_name = self.__class__.__name__
    #     attrs = ', '.join(f'{k}={v!r}' for k, v in self.__dict__.items())
    #     return f'{cls_name}({attrs})'

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        return NotImplemented

    def __gt__(self, other: object) -> bool:
        if isinstance(other, Point):
            return (self.x ** 2 + self.y ** 2) > (other.x ** 2 + other.y ** 2)
        return NotImplemented

# if __name__ == '__main__':
#     x_val = 3.0
#     y_val = 4.5
#     point_instance = Point(x=x_val, y=y_val)
#     print(str(point_instance))
#     point_instance.set_x(new_x=7.0)
#     point_instance.set_y(new_y=8.5)
#     print(str(point_instance))
#     another_point = Point(x=7.0, y=8.5)
#     print(point_instance == another_point)
#     print(repr(point_instance))
#     print(point_instance > Point(x=1.0, y=1.0))
