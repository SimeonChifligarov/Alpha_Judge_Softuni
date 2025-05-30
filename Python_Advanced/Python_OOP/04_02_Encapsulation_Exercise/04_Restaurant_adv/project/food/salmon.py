from project.food.main_dish import MainDish


class Salmon(MainDish):
    """
    This class is about a salmon dish.
    """

    GRAMS: int = 22

    def __init__(self, name: str, price: float) -> None:
        super().__init__(name=name, price=price, grams=self.GRAMS)


if __name__ == '__main__':
    pass

