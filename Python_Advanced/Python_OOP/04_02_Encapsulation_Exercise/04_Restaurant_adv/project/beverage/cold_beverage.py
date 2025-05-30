from project.beverage.beverage import Beverage


class ColdBeverage(Beverage):
    """
    This class is about a cold beverage.
    """

    def __init__(self, name: str, price: float, milliliters: float) -> None:
        super().__init__(name=name, price=price, milliliters=milliliters)


if __name__ == '__main__':
    pass

