from project.beverage.hot_beverage import HotBeverage


class Coffee(HotBeverage):
    """
    This class is about coffee with caffeine amount.

    Args:
        name (str): The name of the coffee.
        caffeine (float): The caffeine of the coffee.
    """

    MILLILITERS: int = 50
    PRICE: float = 3.50

    def __init__(self, name: str, caffeine: float) -> None:
        super().__init__(name=name, price=self.PRICE, milliliters=self.MILLILITERS)
        self.__caffeine = caffeine

    @property
    def caffeine(self) -> float:
        return self.__caffeine


if __name__ == '__main__':
    pass
