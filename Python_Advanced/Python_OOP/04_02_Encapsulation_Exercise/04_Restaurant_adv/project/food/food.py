from project.product import Product


class Food(Product):
    """
    This class is about food with grams.

    Args:
        name (str): The name of the food.
        price (float): The price of the food.
        grams (float): The grams of the food.
    """

    def __init__(self, name: str, price: float, grams: float) -> None:
        super().__init__(name=name, price=price)
        self.__grams = grams

    @property
    def grams(self) -> float:
        return self.__grams


if __name__ == '__main__':
    pass
