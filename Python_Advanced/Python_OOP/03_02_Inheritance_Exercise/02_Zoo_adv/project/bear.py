from project.mammal import Mammal


class Bear(Mammal):
    """
    This class is about a bear that is a kind of mammal.

    Args:
        name (str): The name of the bear.
    """

    def __init__(self, name: str) -> None:
        super().__init__(name=name)

    def __str__(self) -> str:
        return f'Bear(name={self.name})'

    def __repr__(self) -> str:
        return f'Bear(name={self.name})'

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Bear):
            return False
        return self.name == other.name

    def __hash__(self) -> int:
        return hash(self.name)


if __name__ == '__main__':
    # bear_instance = Bear(name='Baloo')
    # print(bear_instance.name)
    pass
