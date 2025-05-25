from project.animal import Animal


class Reptile(Animal):
    """
    This class is about a reptile that is a kind of animal.

    Args:
        name (str): The name of the reptile.
    """

    def __init__(self, name: str) -> None:
        super().__init__(name=name)

    def __str__(self) -> str:
        return f'Reptile(name={self.name})'

    def __repr__(self) -> str:
        return f'Reptile(name={self.name})'

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Reptile):
            return False
        return self.name == other.name

    def __hash__(self) -> int:
        return hash(self.name)


if __name__ == '__main__':
    # reptile_instance = Reptile(name='Rango')
    # print(reptile_instance.name)
    pass
