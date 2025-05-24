from project.animal import Animal


class Cat(Animal):
    """
    This class is about a cat that can meow and eat.

    Methods:
        meow(): Says that the cat is meowing.
    """

    def meow(self) -> str:
        return 'meowing...'


if __name__ == '__main__':
    # cat_instance = Cat()
    # print(cat_instance.meow())
    pass
