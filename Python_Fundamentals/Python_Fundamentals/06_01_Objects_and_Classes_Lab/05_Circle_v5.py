class Circle:
    __pi = 3.14

    def __init__(self, diameter: float):
        """Initializes the circle with its diameter and calculates radius."""
        self.diameter = diameter
        self.radius = diameter / 2

    def calculate_circumference(self) -> float:
        """Returns the circumference of the circle."""
        return 2 * Circle.__pi * self.radius

    def calculate_area(self) -> float:
        """Returns the area of the circle."""
        return Circle.__pi * (self.radius ** 2)

    def calculate_area_of_sector(self, angle: float) -> float:
        """Returns the area of a sector given its central angle in degrees."""
        return (angle / 360) * self.calculate_area()
