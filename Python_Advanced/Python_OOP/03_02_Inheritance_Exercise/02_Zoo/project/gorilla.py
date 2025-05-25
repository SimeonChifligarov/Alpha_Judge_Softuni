from project.mammal import Mammal


class Gorilla(Mammal):
    """
    This class is about a gorilla that is a kind of mammal.

    Args:
        name (str): The name of the gorilla.
    """

    def __init__(self, name: str) -> None:
        super().__init__(name=name)


if __name__ == '__main__':
    # gorilla_instance = Gorilla(name='Koko')
    # print(gorilla_instance.name)
    pass
