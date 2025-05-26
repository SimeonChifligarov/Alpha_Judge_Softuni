from project.product import Product


class Drink(Product):
    """
    This class is about a drink which is a type of product.

    Args:
        name (str): The name of the drink.
    """

    def __init__(self, name: str) -> None:
        super().__init__(name=name, quantity=10)


if __name__ == '__main__':
    # drink_instance = Drink(name='water')
    pass
