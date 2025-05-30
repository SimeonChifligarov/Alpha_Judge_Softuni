from project.food.food import Food


class Dessert(Food):
    """
    This class is about a dessert with calories.

    Args:
        name (str): The name of the dessert.
        price (float): The price of the dessert.
        grams (float): The grams of the dessert.
        calories (float): The calories of the dessert.
    """

    def __init__(self, name: str, price: float, grams: float, calories: float) -> None:
        super().__init__(name=name, price=price, grams=grams)
        self.__calories = calories

    @property
    def calories(self) -> float:
        return self.__calories


if __name__ == '__main__':
    pass
