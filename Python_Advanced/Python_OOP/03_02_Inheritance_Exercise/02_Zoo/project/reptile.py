from project.animal import Animal


class Reptile(Animal):
    """
    This class is about a reptile that is a kind of animal.

    Args:
        name (str): The name of the reptile.
    """

    def __init__(self, name: str) -> None:
        super().__init__(name=name)


if __name__ == '__main__':
    # reptile_instance = Reptile(name='Rango')
    # print(reptile_instance.name)
    pass
