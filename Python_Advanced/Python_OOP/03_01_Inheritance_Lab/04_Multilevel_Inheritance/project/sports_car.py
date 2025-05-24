from project.car import Car


class SportsCar(Car):
    """
    This class is about a sports car that can race.

    Methods:
        race(): Says that the sports car is racing.
    """

    def race(self) -> str:
        return 'racing...'


if __name__ == '__main__':
    # sports_car_instance = SportsCar()
    # print(sports_car_instance.race())
    pass
