from project.product import Product


class Beverage(Product):
    """
    This class is about a beverage with milliliters.

    Args:
        name (str): The name of the beverage.
        price (float): The price of the beverage.
        milliliters (float): The milliliters of the beverage.
    """

    def __init__(self, name: str, price: float, milliliters: float) -> None:
        super().__init__(name=name, price=price)
        self.__milliliters = milliliters

    @property
    def milliliters(self) -> float:
        return self.__milliliters


if __name__ == '__main__':
    pass
