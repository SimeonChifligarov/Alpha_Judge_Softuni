from abc import ABC


class Food(ABC):
    """
    This class represents an abstract food.

    Args:
        quantity (int): The quantity of food.
    """

    def __init__(self, quantity: int) -> None:
        self.quantity = quantity


class Vegetable(Food):
    """
    This class represents a vegetable.
    """
    pass


class Fruit(Food):
    """
    This class represents a fruit.
    """
    pass


class Meat(Food):
    """
    This class represents meat.
    """
    pass


class Seed(Food):
    """
    This class represents a seed.
    """
    pass
