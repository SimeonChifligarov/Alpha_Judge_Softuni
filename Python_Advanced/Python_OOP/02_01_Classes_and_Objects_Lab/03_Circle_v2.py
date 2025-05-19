class Circle:
    """
    This class is for a circle. It stores the radius and calculates area and circumference.

    Args:
        radius (float): The radius of the circle
    """

    pi = 3.14

    def __init__(self, radius: float) -> None:
        self.radius = radius

    def set_radius(self, new_radius: float) -> None:
        """
        This method sets a new radius.

        Args:
            new_radius (float): The new radius value
        """
        self.radius = new_radius

    def get_area(self) -> float:
        """
        This method calculates the area of the circle.

        Returns:
            float: The area
        """
        return Circle.pi * self.radius ** 2

    def get_circumference(self) -> float:
        """
        This method calculates the circumference of the circle.

        Returns:
            float: The circumference
        """
        return 2 * Circle.pi * self.radius

# if __name__ == '__main__':
#     circle_radius = 5.0
#     circle_instance = Circle(radius=circle_radius)
#     print(circle_instance.get_area())
#     print(circle_instance.get_circumference())
#     circle_instance.set_radius(new_radius=10.0)
#     print(circle_instance.get_area())
#     print(circle_instance.get_circumference())
