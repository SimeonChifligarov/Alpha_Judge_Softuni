from project.vehicle import Vehicle


class Car(Vehicle):
    """
    This class is about a car which is a type of vehicle.

    Args:
        fuel (float): The amount of fuel.
        horse_power (int): The horsepower of the car.
    """

    DEFAULT_FUEL_CONSUMPTION: float = 3

    def __init__(self, fuel: float, horse_power: int) -> None:
        super().__init__(fuel=fuel, horse_power=horse_power)
        self.fuel_consumption = self.DEFAULT_FUEL_CONSUMPTION

    def __str__(self) -> str:
        return f'Car(fuel={self.fuel}, horse_power={self.horse_power})'

    def __repr__(self) -> str:
        return f'Car(fuel={self.fuel}, horse_power={self.horse_power})'


if __name__ == '__main__':
    # car_instance = Car(fuel=50.0, horse_power=150)
    pass
