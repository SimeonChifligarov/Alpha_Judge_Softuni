from project.dough import Dough
from project.topping import Topping


class Pizza:
    """
    This class is about a pizza that has a name, dough, toppings and a limit on number of toppings.

    Args:
        name (str): The name of the pizza.
        dough (Dough): The dough used for the pizza.
        max_number_of_toppings (int): The maximum number of toppings allowed.
    """

    def __init__(self, name: str, dough: Dough, max_number_of_toppings: int) -> None:
        self.name = name
        self.dough = dough
        self.max_number_of_toppings = max_number_of_toppings
        self.toppings: dict[str, float] = {}

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value: str) -> None:
        if value == '':
            raise ValueError('The name cannot be an empty string')
        self.__name = value

    @property
    def dough(self) -> Dough:
        return self.__dough

    @dough.setter
    def dough(self, value: Dough) -> None:
        if value is None:
            raise ValueError('You should add dough to the pizza')
        self.__dough = value

    @property
    def max_number_of_toppings(self) -> int:
        return self.__max_number_of_toppings

    @max_number_of_toppings.setter
    def max_number_of_toppings(self, value: int) -> None:
        if value <= 0:
            raise ValueError('The maximum number of toppings cannot be less or equal to zero')
        self.__max_number_of_toppings = value

    def add_topping(self, topping: Topping) -> None:
        if len(self.toppings) >= self.max_number_of_toppings:
            raise ValueError('Not enough space for another topping')
        if topping.topping_type not in self.toppings:
            self.toppings[topping.topping_type] = 0
        self.toppings[topping.topping_type] += topping.weight

    def calculate_total_weight(self) -> float:
        toppings_weight = sum(self.toppings.values())
        return self.dough.weight + toppings_weight


if __name__ == '__main__':
    pass
