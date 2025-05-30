from project.food.food import Food


class MainDish(Food):
    """
    This class is about a main dish.
    """

    def __init__(self, name: str, price: float, grams: float) -> None:
        super().__init__(name=name, price=price, grams=grams)


if __name__ == '__main__':
    pass
