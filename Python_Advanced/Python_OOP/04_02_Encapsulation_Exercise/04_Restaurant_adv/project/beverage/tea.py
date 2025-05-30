from project.beverage.hot_beverage import HotBeverage


class Tea(HotBeverage):
    """
    This class is about tea.

    Args:
        name (str): The name of the tea.
        price (float): The price of the tea.
        milliliters (float): The milliliters of the tea.
    """

    def __init__(self, name: str, price: float, milliliters: float) -> None:
        super().__init__(name=name, price=price, milliliters=milliliters)


if __name__ == '__main__':
    pass

