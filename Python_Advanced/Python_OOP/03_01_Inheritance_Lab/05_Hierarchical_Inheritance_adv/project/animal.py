class Animal:
    """
    This class is about an animal that can eat.

    Methods:
        eat(): Says that the animal is eating.
    """

    # def eat(self) -> str:
    #     return 'eating...'

    @staticmethod
    def eat() -> str:
        return 'eating...'

    def __str__(self) -> str:
        return 'Animal()'

    def __repr__(self) -> str:
        return 'Animal()'

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Animal)

    def __hash__(self) -> int:
        return hash('Animal')


if __name__ == '__main__':
    # animal_instance = Animal()
    # print(animal_instance.eat())
    pass
