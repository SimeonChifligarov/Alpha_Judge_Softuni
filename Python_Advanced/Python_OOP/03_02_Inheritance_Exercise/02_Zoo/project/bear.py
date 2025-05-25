from project.mammal import Mammal


class Bear(Mammal):
    """
    This class is about a bear that is a kind of mammal.

    Args:
        name (str): The name of the bear.
    """

    def __init__(self, name: str) -> None:
        super().__init__(name=name)


if __name__ == '__main__':
    # bear_instance = Bear(name='Baloo')
    # print(bear_instance.name)
    pass
