from project.animal import Animal


class Cat(Animal):
    """
    This class is about a cat that can meow and eat.

    Methods:
        meow(): Says that the cat is meowing.
    """

    # def meow(self) -> str:
    #     return 'meowing...'

    @staticmethod
    def meow() -> str:
        return 'meowing...'

    def __str__(self) -> str:
        return 'Cat()'

    def __repr__(self) -> str:
        return 'Cat()'

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Cat)

    def __hash__(self) -> int:
        return hash('Cat')


if __name__ == '__main__':
    # cat_instance = Cat()
    # print(cat_instance.meow())
    pass
