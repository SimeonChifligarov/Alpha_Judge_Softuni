class Product:
    """
    This class is about a product that has a name and a quantity.

    Args:
        name (str): The name of the product.
        quantity (int): The quantity of the product.
    """

    def __init__(self, name: str, quantity: int) -> None:
        self.name = name
        self.quantity = quantity

    def decrease(self, quantity: int) -> None:
        if quantity > self.quantity:
            return
        self.quantity -= quantity

    def increase(self, quantity: int) -> None:
        self.quantity += quantity

    def __repr__(self) -> str:
        return f'{self.name}'


if __name__ == '__main__':
    # product_instance = Product(name='apple', quantity=10)
    pass
