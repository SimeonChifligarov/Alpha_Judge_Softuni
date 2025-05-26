class Vehicle:
    """
    This class is about a simple vehicle that has fuel and horsepower.

    Args:
        fuel (float): The amount of fuel.
        horse_power (int): The horsepower of the vehicle.
    """

    DEFAULT_FUEL_CONSUMPTION: float = 1.25

    def __init__(self, fuel: float, horse_power: int) -> None:
        self.fuel_consumption: float = self.DEFAULT_FUEL_CONSUMPTION
        self.fuel: float = fuel
        self.horse_power: int = horse_power

    def drive(self, kilometers: float) -> None:
        needed_fuel = kilometers * self.fuel_consumption
        if needed_fuel > self.fuel:
            return
        self.fuel -= needed_fuel

    def __str__(self) -> str:
        return f'Vehicle(fuel={self.fuel}, horse_power={self.horse_power})'

    def __repr__(self) -> str:
        return f'Vehicle(fuel={self.fuel}, horse_power={self.horse_power})'

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Vehicle):
            return False
        return self.fuel == other.fuel and self.horse_power == other.horse_power

    def __hash__(self) -> int:
        return hash((self.fuel, self.horse_power))


if __name__ == '__main__':
    # vehicle_instance = Vehicle(fuel=100.0, horse_power=120)
    pass
