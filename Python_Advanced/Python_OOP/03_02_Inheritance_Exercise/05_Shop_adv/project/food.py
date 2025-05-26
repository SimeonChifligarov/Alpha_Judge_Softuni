from project.product import Product


class Food(Product):
    """
    This class is about food which is a type of product.

    Args:
        name (str): The name of the food.
    """

    def __init__(self, name: str) -> None:
        super().__init__(name=name, quantity=15)


if __name__ == '__main__':
    # food_instance = Food(name='apple')
    pass
