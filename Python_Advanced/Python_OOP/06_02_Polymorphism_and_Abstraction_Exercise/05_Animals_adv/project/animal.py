from abc import ABC, abstractmethod


class Animal(ABC):
    """
    This class represents an abstract animal.

    Args:
        name (str): The name of the animal.
        age (int): The age of the animal.
        gender (str): The gender of the animal.
    """

    def __init__(self, name: str, age: int, gender: str) -> None:
        self.name = name
        self.age = age
        self.gender = gender

    @abstractmethod
    def make_sound(self) -> str:
        pass

    @abstractmethod
    def __repr__(self) -> str:
        pass
