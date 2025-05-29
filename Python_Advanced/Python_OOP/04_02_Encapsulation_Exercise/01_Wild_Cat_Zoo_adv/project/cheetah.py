from project.animal import Animal


class Cheetah(Animal):
    """
    This class is about a cheetah.

    Args:
        name (str): The name of the cheetah.
        gender (str): The gender of the cheetah.
        age (int): The age of the cheetah.
    """

    def __init__(self, name: str, gender: str, age: int) -> None:
        super().__init__(name=name, gender=gender, age=age, money_for_care=60)


if __name__ == '__main__':
    pass
