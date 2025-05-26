from project.vehicle import Vehicle


class Motorcycle(Vehicle):
    """
    This class is about a motorcycle which is a type of vehicle.

    Args:
        fuel (float): The amount of fuel.
        horse_power (int): The horsepower of the motorcycle.
    """

    def __init__(self, fuel: float, horse_power: int) -> None:
        super().__init__(fuel=fuel, horse_power=horse_power)

    def __str__(self) -> str:
        return f'Motorcycle(fuel={self.fuel}, horse_power={self.horse_power})'

    def __repr__(self) -> str:
        return f'Motorcycle(fuel={self.fuel}, horse_power={self.horse_power})'


if __name__ == '__main__':
    # motorcycle_instance = Motorcycle(fuel=40.0, horse_power=100)
    pass
