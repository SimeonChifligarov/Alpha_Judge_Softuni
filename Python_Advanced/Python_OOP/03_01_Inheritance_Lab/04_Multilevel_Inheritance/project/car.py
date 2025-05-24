from project.vehicle import Vehicle


class Car(Vehicle):
    """
    This class is about a car that can drive.

    Methods:
        drive(): Says that the car is driving.
    """

    def drive(self) -> str:
        return 'driving...'


if __name__ == '__main__':
    # car_instance = Car()
    # print(car_instance.drive())
    pass
