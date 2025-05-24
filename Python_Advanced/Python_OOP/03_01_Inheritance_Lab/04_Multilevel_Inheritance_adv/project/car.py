from project.vehicle import Vehicle


class Car(Vehicle):
    """
    This class is about a car that can drive.

    Methods:
        drive(): Says that the car is driving.
    """

    # def drive(self) -> str:
    #     return 'driving...'

    @staticmethod
    def drive() -> str:
        return 'driving...'

    def __str__(self) -> str:
        return 'Car()'

    def __repr__(self) -> str:
        return 'Car()'

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Car)

    def __hash__(self) -> int:
        return hash('Car')


if __name__ == '__main__':
    # car_instance = Car()
    # print(car_instance.drive())
    pass
