class Animal:
    """
    This class is about an animal that has a name.

    Args:
        name (str): The name of the animal.
    """

    def __init__(self, name: str) -> None:
        self.name = name

    def __str__(self) -> str:
        return f'Animal(name={self.name})'

    def __repr__(self) -> str:
        return f'Animal(name={self.name})'

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Animal):
            return False
        return self.name == other.name

    def __hash__(self) -> int:
        return hash(self.name)


if __name__ == '__main__':
    # animal_instance = Animal(name='Buddy')
    # print(animal_instance.name)
    pass
