class Vehicle:
    """
    This class is about a vehicle that can move.

    Methods:
        move(): Says that the vehicle is moving.
    """

    # def move(self) -> str:
    #     return 'moving...'

    @staticmethod
    def move() -> str:
        return 'moving...'

    def __str__(self) -> str:
        return 'Vehicle()'

    def __repr__(self) -> str:
        return 'Vehicle()'

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Vehicle)

    def __hash__(self) -> int:
        return hash('Vehicle')


if __name__ == '__main__':
    # vehicle_instance = Vehicle()
    # print(vehicle_instance.move())
    pass
