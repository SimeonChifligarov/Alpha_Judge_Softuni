from project.mammal import Mammal


class Gorilla(Mammal):
    """
    This class is about a gorilla that is a kind of mammal.

    Args:
        name (str): The name of the gorilla.
    """

    def __init__(self, name: str) -> None:
        super().__init__(name=name)

    def __str__(self) -> str:
        return f'Gorilla(name={self.name})'

    def __repr__(self) -> str:
        return f'Gorilla(name={self.name})'

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Gorilla):
            return False
        return self.name == other.name

    def __hash__(self) -> int:
        return hash(self.name)


if __name__ == '__main__':
    # gorilla_instance = Gorilla(name='Koko')
    # print(gorilla_instance.name)
    pass
