from project.reptile import Reptile


class Lizard(Reptile):
    """
    This class is about a lizard that is a kind of reptile.

    Args:
        name (str): The name of the lizard.
    """

    def __init__(self, name: str) -> None:
        super().__init__(name=name)


if __name__ == '__main__':
    # lizard_instance = Lizard(name='Spike')
    # print(lizard_instance.name)
    pass
