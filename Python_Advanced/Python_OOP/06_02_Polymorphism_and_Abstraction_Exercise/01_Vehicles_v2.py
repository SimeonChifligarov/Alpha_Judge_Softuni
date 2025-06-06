from abc import ABC, abstractmethod
from typing import Any


class Vehicle(ABC):
    """
    This class represents an abstract vehicle.
    """

    def __init__(self, fuel_quantity: float, fuel_consumption: float) -> None:
        self.__fuel_quantity = fuel_quantity
        self.__fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self, distance: float) -> Any:
        """
        Drive the vehicle a given distance.

        Args:
            distance (float): The distance to drive.
        """
        pass

    @abstractmethod
    def refuel(self, fuel: float) -> Any:
        """
        Refuel the vehicle.

        Args:
            fuel (float): The amount of fuel to add.
        """
        pass

    @property
    def fuel_quantity(self) -> float:
        return self.__fuel_quantity

    @fuel_quantity.setter
    def fuel_quantity(self, value: float) -> None:
        self.__fuel_quantity = value

    @property
    def fuel_consumption(self) -> float:
        return self.__fuel_consumption

    @fuel_consumption.setter
    def fuel_consumption(self, value: float) -> None:
        self.__fuel_consumption = value


class Car(Vehicle):
    """
    This class represents a car.
    """

    def drive(self, distance: float) -> None:
        total_consumption = (self.fuel_consumption + 0.9) * distance
        if self.fuel_quantity >= total_consumption:
            self.fuel_quantity -= total_consumption

    def refuel(self, fuel: float) -> None:
        if fuel <= 0:
            return
        self.fuel_quantity += fuel


class Truck(Vehicle):
    """
    This class represents a truck.
    """

    def drive(self, distance: float) -> None:
        total_consumption = (self.fuel_consumption + 1.6) * distance
        if self.fuel_quantity >= total_consumption:
            self.fuel_quantity -= total_consumption

    def refuel(self, fuel: float) -> None:
        if fuel <= 0:
            return
        self.fuel_quantity += fuel * 0.95


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
