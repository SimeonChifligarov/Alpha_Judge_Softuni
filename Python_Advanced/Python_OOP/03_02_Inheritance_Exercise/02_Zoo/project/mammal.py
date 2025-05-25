from project.animal import Animal


class Mammal(Animal):
    """
    This class is about a mammal that is a kind of animal.

    Args:
        name (str): The name of the mammal.
    """

    def __init__(self, name: str) -> None:
        super().__init__(name=name)


if __name__ == '__main__':
    # mammal_instance = Mammal(name='Stella')
    # print(mammal_instance.name)
    pass
