from abc import ABC, abstractmethod
from project.food import Food


class Animal(ABC):
    """
    This class represents an abstract animal.

    Args:
        name (str): The name of the animal.
        weight (float): The weight of the animal.
    """

    def __init__(self, name: str, weight: float) -> None:
        self.name = name
        self.weight = weight
        self.food_eaten = 0

    @abstractmethod
    def make_sound(self) -> str:
        pass

    @abstractmethod
    def feed(self, food: Food) -> str:
        pass


class Bird(Animal):
    """
    This class represents an abstract bird.

    Args:
        wing_size (float): The wing size of the bird.
    """

    def __init__(self, name: str, weight: float, wing_size: float) -> None:
        super().__init__(name=name, weight=weight)
        self.wing_size = wing_size

    def __repr__(self) -> str:
        return f'{self.__class__.__name__} [{self.name}, {self.wing_size}, {self.weight}, {self.food_eaten}]'


class Mammal(Animal):
    """
    This class represents an abstract mammal.

    Args:
        living_region (str): The region where the mammal lives.
    """

    def __init__(self, name: str, weight: float, living_region: str) -> None:
        super().__init__(name=name, weight=weight)
        self.living_region = living_region

    def __repr__(self) -> str:
        return f'{self.__class__.__name__} [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]'
