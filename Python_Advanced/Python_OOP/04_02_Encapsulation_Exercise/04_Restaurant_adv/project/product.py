class Product:
    """
    This class is about a product with a name and price.

    Args:
        name (str): The name of the product.
        price (float): The price of the product.
    """

    def __init__(self, name: str, price: float) -> None:
        self.__name = name
        self.__price = price

    @property
    def name(self) -> str:
        return self.__name

    @property
    def price(self) -> float:
        return self.__price


if __name__ == '__main__':
    pass
