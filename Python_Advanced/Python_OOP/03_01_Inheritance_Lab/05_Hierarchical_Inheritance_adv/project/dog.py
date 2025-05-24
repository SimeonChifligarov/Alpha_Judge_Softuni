from project.animal import Animal


class Dog(Animal):
    """
    This class is about a dog that can bark and eat.

    Methods:
        bark(): Says that the dog is barking.
    """

    # def bark(self) -> str:
    #     return 'barking...'

    @staticmethod
    def bark() -> str:
        return 'barking...'

    def __str__(self) -> str:
        return 'Dog()'

    def __repr__(self) -> str:
        return 'Dog()'

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Dog)

    def __hash__(self) -> int:
        return hash('Dog')


if __name__ == '__main__':
    # dog_instance = Dog()
    # print(dog_instance.bark())
    pass
