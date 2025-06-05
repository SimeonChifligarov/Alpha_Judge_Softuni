from abc import ABC, abstractmethod
from typing import Any
import math


class Shape(ABC):
    """
    This class represents an abstract shape.
    """

    @abstractmethod
    def calculate_area(self) -> Any:
        """
        Calculate the area of the shape.

        Returns:
            Any: The area.
        """
        pass

    @abstractmethod
    def calculate_perimeter(self) -> Any:
        """
        Calculate the perimeter of the shape.

        Returns:
            Any: The perimeter.
        """
        pass


class Circle(Shape):
    """
    This class represents a circle.

    Args:
        radius (float): The radius of the circle.
    """

    def __init__(self, radius: float) -> None:
        self.__radius = radius

    def __repr__(self) -> str:
        return f'Circle(radius={self.__radius})'

    def __str__(self) -> str:
        return f'Circle with radius {self.__radius}'

    def __hash__(self) -> int:
        return hash(self.__radius)

    def calculate_area(self) -> float:
        return math.pi * (self.__radius ** 2)

    def calculate_perimeter(self) -> float:
        return 2 * math.pi * self.__radius


class Rectangle(Shape):
    """
    This class represents a rectangle.

    Args:
        height (float): The height of the rectangle.
        width (float): The width of the rectangle.
    """

    def __init__(self, height: float, width: float) -> None:
        self.__height = height
        self.__width = width

    def __repr__(self) -> str:
        return f'Rectangle(height={self.__height}, width={self.__width})'

    def __str__(self) -> str:
        return f'Rectangle with height {self.__height} and width {self.__width}'

    def __hash__(self) -> int:
        return hash((self.__height, self.__width))

    def calculate_area(self) -> float:
        return self.__height * self.__width

    def calculate_perimeter(self) -> float:
        return 2 * (self.__height + self.__width)


if __name__ == '__main__':
    # circle_instance = Circle(radius=5)
    # print(circle_instance.calculate_area())
    # print(circle_instance.calculate_perimeter())
    #
    # rectangle_instance = Rectangle(height=10, width=20)
    # print(rectangle_instance.calculate_area())
    # print(rectangle_instance.calculate_perimeter())
    pass
