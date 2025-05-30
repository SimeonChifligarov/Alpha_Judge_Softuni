from project.food.dessert import Dessert


class Cake(Dessert):
    """
    This class is about a cake dessert.
    """

    GRAMS: int = 250
    CALORIES: int = 1000
    PRICE: float = 5

    def __init__(self, name: str) -> None:
        super().__init__(name=name, price=self.PRICE, grams=self.GRAMS, calories=self.CALORIES)


if __name__ == '__main__':
    pass

