from abc import ABC, abstractmethod


class Vehicle(ABC):
    """
    This class represents an abstract vehicle.

    Args:
        fuel_quantity (float): How much fuel the vehicle has.
        fuel_consumption (float): How much fuel the vehicle uses per km.
    """

    def __init__(self, fuel_quantity: float, fuel_consumption: float) -> None:
        self._fuel_quantity = fuel_quantity
        self._fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self, distance: float) -> None:
        """
        Drive the vehicle a given distance.

        Args:
            distance (float): The distance to drive.
        """
        pass

    @abstractmethod
    def refuel(self, fuel: float) -> None:
        """
        Refuel the vehicle with a given amount.

        Args:
            fuel (float): The amount of fuel to add.
        """
        pass

    @property
    def fuel_quantity(self) -> float:
        return self._fuel_quantity

    @fuel_quantity.setter
    def fuel_quantity(self, value: float) -> None:
        self._fuel_quantity = value

    @property
    def fuel_consumption(self) -> float:
        return self._fuel_consumption

    @fuel_consumption.setter
    def fuel_consumption(self, value: float) -> None:
        self._fuel_consumption = value


class Car(Vehicle):
    """
    This class represents a car.
    """

    _increased_consumption_to_add: float = 0.9

    def drive(self, distance: float) -> None:
        needed_fuel = distance * (self.fuel_consumption + Car._increased_consumption_to_add)
        if self.fuel_quantity < needed_fuel:
            return
        self.fuel_quantity -= needed_fuel

    def refuel(self, fuel: float) -> None:
        if fuel <= 0:
            return
        self.fuel_quantity += fuel


class Truck(Vehicle):
    """
    This class represents a truck.
    """

    _increased_consumption_to_add: float = 1.6
    _fuel_lost_from_hole_proportion: float = 0.05

    def drive(self, distance: float) -> None:
        needed_fuel = distance * (self.fuel_consumption + Truck._increased_consumption_to_add)
        if self.fuel_quantity < needed_fuel:
            return
        self.fuel_quantity -= needed_fuel

    def refuel(self, fuel: float) -> None:
        if fuel <= 0:
            return
        self.fuel_quantity += fuel * (1 - Truck._fuel_lost_from_hole_proportion)


if __name__ == '__main__':
    # car_instance = Car(fuel_quantity=20, fuel_consumption=5)
    # car_instance.drive(distance=3)
    # print(car_instance.fuel_quantity)
    # car_instance.refuel(fuel=10)
    # print(car_instance.fuel_quantity)
    #
    # truck_instance = Truck(fuel_quantity=100, fuel_consumption=15)
    # truck_instance.drive(distance=5)
    # print(truck_instance.fuel_quantity)
    # truck_instance.refuel(fuel=50)
    # print(truck_instance.fuel_quantity)
    pass
