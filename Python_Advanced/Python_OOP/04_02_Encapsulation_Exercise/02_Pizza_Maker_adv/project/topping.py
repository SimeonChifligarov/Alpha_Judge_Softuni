class Topping:
    """
    This class is about a pizza topping that has a type and weight.

    Args:
        topping_type (str): The type of the topping.
        weight (float): The weight of the topping.
    """

    def __init__(self, topping_type: str, weight: float) -> None:
        self.topping_type = topping_type
        self.weight = weight

    @property
    def topping_type(self) -> str:
        return self.__topping_type

    @topping_type.setter
    def topping_type(self, value: str) -> None:
        if value == '':
            raise ValueError('The topping type cannot be an empty string')
        self.__topping_type = value

    @property
    def weight(self) -> float:
        return self.__weight

    @weight.setter
    def weight(self, value: float) -> None:
        if value <= 0:
            raise ValueError('The weight cannot be less or equal to zero')
        self.__weight = value


if __name__ == '__main__':
    pass
