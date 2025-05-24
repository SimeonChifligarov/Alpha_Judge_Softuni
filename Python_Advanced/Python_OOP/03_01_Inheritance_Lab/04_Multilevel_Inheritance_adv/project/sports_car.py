from project.car import Car


class SportsCar(Car):
    """
    This class is about a sports car that can race.

    Methods:
        race(): Says that the sports car is racing.
    """

    # def race(self) -> str:
    #     return 'racing...'

    @staticmethod
    def race() -> str:
        return 'racing...'

    def __str__(self) -> str:
        return 'SportsCar()'

    def __repr__(self) -> str:
        return 'SportsCar()'

    def __eq__(self, other: object) -> bool:
        return isinstance(other, SportsCar)

    def __hash__(self) -> int:
        return hash('SportsCar')


if __name__ == '__main__':
    # sports_car_instance = SportsCar()
    # print(sports_car_instance.race())
    pass
