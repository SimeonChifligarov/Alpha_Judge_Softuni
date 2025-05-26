from project.motorcycle import Motorcycle


class CrossMotorcycle(Motorcycle):
    """
    This class is about a cross motorcycle which is a type of motorcycle.

    Args:
        fuel (float): The amount of fuel.
        horse_power (int): The horsepower of the cross motorcycle.
    """

    def __init__(self, fuel: float, horse_power: int) -> None:
        super().__init__(fuel=fuel, horse_power=horse_power)

    def __str__(self) -> str:
        return f'CrossMotorcycle(fuel={self.fuel}, horse_power={self.horse_power})'

    def __repr__(self) -> str:
        return f'CrossMotorcycle(fuel={self.fuel}, horse_power={self.horse_power})'


if __name__ == '__main__':
    # cross_motorcycle_instance = CrossMotorcycle(fuel=35.0, horse_power=90)
    pass
