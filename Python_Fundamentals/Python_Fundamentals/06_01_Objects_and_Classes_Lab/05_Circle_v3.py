class Circle:
    """
    Represents a circle with methods to calculate circumference, area, and sector area.
    """

    __pi = 3.14

    def __init__(self, diameter: float) -> None:
        self.radius = diameter / 2

    @property
    def diameter(self) -> float:
        return self.radius * 2

    def calculate_circumference(self) -> float:
        return 2 * self.__pi * self.radius

    def calculate_area(self) -> float:
        return self.__pi * (self.radius ** 2)

    def calculate_area_of_sector(self, angle: float) -> float:
        return (angle / 360) * self.__pi * (self.radius ** 2)

# if __name__ == '__main__':
#     circle_instance = Circle(diameter=float(input()))
#     print(circle_instance.calculate_circumference())
#     print(circle_instance.calculate_area())
#     print(circle_instance.calculate_area_of_sector(angle=float(input())))
