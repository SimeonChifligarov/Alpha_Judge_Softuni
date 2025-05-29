from project.animal import Animal


class Tiger(Animal):
    """
    This class is about a tiger.

    Args:
        name (str): The name of the tiger.
        gender (str): The gender of the tiger.
        age (int): The age of the tiger.
    """

    def __init__(self, name: str, gender: str, age: int) -> None:
        super().__init__(name=name, gender=gender, age=age, money_for_care=45)


if __name__ == '__main__':
    pass
