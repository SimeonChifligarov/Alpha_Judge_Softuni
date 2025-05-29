class Animal:
    """
    This class is about an animal that lives in the zoo.

    Args:
        name (str): The name of the animal.
        gender (str): The gender of the animal.
        age (int): The age of the animal.
        money_for_care (int): The money needed for the animal care.
    """

    def __init__(self, name: str, gender: str, age: int, money_for_care: int) -> None:
        self.name = name
        self.gender = gender
        self.age = age
        self.money_for_care = money_for_care

    def __repr__(self) -> str:
        return f'Name: {self.name}, Age: {self.age}, Gender: {self.gender}'


if __name__ == '__main__':
    pass
