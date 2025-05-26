from project.car import Car


class FamilyCar(Car):
    """
    This class is about a family car which is a type of car.

    Args:
        fuel (float): The amount of fuel.
        horse_power (int): The horsepower of the family car.
    """

    def __init__(self, fuel: float, horse_power: int) -> None:
        super().__init__(fuel=fuel, horse_power=horse_power)

    def __str__(self) -> str:
        return f'FamilyCar(fuel={self.fuel}, horse_power={self.horse_power})'

    def __repr__(self) -> str:
        return f'FamilyCar(fuel={self.fuel}, horse_power={self.horse_power})'


if __name__ == '__main__':
    # family_car_instance = FamilyCar(fuel=70.0, horse_power=140)
    pass
