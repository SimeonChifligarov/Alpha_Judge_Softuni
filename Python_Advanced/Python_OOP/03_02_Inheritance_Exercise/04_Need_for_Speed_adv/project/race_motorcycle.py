from project.motorcycle import Motorcycle


class RaceMotorcycle(Motorcycle):
    """
    This class is about a race motorcycle which is a type of motorcycle.

    Args:
        fuel (float): The amount of fuel.
        horse_power (int): The horsepower of the race motorcycle.
    """

    DEFAULT_FUEL_CONSUMPTION: float = 8

    def __init__(self, fuel: float, horse_power: int) -> None:
        super().__init__(fuel=fuel, horse_power=horse_power)
        self.fuel_consumption = self.DEFAULT_FUEL_CONSUMPTION

    def __str__(self) -> str:
        return f'RaceMotorcycle(fuel={self.fuel}, horse_power={self.horse_power})'

    def __repr__(self) -> str:
        return f'RaceMotorcycle(fuel={self.fuel}, horse_power={self.horse_power})'


if __name__ == '__main__':
    # race_motorcycle_instance = RaceMotorcycle(fuel=30.0, horse_power=110)
    pass
