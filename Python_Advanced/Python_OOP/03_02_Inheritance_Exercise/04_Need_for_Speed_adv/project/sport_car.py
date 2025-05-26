from project.car import Car


class SportCar(Car):
    """
    This class is about a sport car which is a type of car.

    Args:
        fuel (float): The amount of fuel.
        horse_power (int): The horsepower of the sport car.
    """

    DEFAULT_FUEL_CONSUMPTION: float = 10

    def __init__(self, fuel: float, horse_power: int) -> None:
        super().__init__(fuel=fuel, horse_power=horse_power)
        self.fuel_consumption = self.DEFAULT_FUEL_CONSUMPTION

    def __str__(self) -> str:
        return f'SportCar(fuel={self.fuel}, horse_power={self.horse_power})'

    def __repr__(self) -> str:
        return f'SportCar(fuel={self.fuel}, horse_power={self.horse_power})'


if __name__ == '__main__':
    # sport_car_instance = SportCar(fuel=60.0, horse_power=300)
    pass
