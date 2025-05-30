from project.beverage.beverage import Beverage


class HotBeverage(Beverage):
    """
    This class is about a hot beverage.
    """

    def __init__(self, name: str, price: float, milliliters: float) -> None:
        super().__init__(name=name, price=price, milliliters=milliliters)


if __name__ == '__main__':
    pass

