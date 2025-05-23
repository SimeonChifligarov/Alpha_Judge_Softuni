from project.animal import Animal


class Dog(Animal):
    """
    This class is about a dog that can bark and eat.

    Methods:
        bark(): Says that the dog is barking.
    """

    def bark(self) -> str:
        return 'barking...'


if __name__ == '__main__':
    # dog_instance = Dog()
    # print(dog_instance.bark())
    pass
