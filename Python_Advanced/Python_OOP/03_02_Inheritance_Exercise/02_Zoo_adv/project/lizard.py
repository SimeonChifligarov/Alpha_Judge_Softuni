from project.reptile import Reptile


class Lizard(Reptile):
    """
    This class is about a lizard that is a kind of reptile.

    Args:
        name (str): The name of the lizard.
    """

    def __init__(self, name: str) -> None:
        super().__init__(name=name)

    def __str__(self) -> str:
        return f'Lizard(name={self.name})'

    def __repr__(self) -> str:
        return f'Lizard(name={self.name})'

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Lizard):
            return False
        return self.name == other.name

    def __hash__(self) -> int:
        return hash(self.name)


if __name__ == '__main__':
    # lizard_instance = Lizard(name='Spike')
    # print(lizard_instance.name)
    pass
