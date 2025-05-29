from project.animal import Animal


class Lion(Animal):
    """
    This class is about a lion.

    Args:
        name (str): The name of the lion.
        gender (str): The gender of the lion.
        age (int): The age of the lion.
    """

    def __init__(self, name: str, gender: str, age: int) -> None:
        super().__init__(name=name, gender=gender, age=age, money_for_care=50)


if __name__ == '__main__':
    pass
