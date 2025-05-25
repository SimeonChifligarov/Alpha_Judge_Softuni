from project.animal import Animal


class Mammal(Animal):
    """
    This class is about a mammal that is a kind of animal.

    Args:
        name (str): The name of the mammal.
    """

    def __init__(self, name: str) -> None:
        super().__init__(name=name)

    def __str__(self) -> str:
        return f'Mammal(name={self.name})'

    def __repr__(self) -> str:
        return f'Mammal(name={self.name})'

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Mammal):
            return False
        return self.name == other.name

    def __hash__(self) -> int:
        return hash(self.name)


if __name__ == '__main__':
    # mammal_instance = Mammal(name='Stella')
    # print(mammal_instance.name)
    pass
