from project.food.starter import Starter


class Soup(Starter):
    """
    This class is about a soup dish.

    Args:
        name (str): The name of the soup.
        price (float): The price of the soup.
        grams (float): The grams of the soup.
    """

    def __init__(self, name: str, price: float, grams: float) -> None:
        super().__init__(name=name, price=price, grams=grams)


if __name__ == '__main__':
    pass

