from project.cat import Cat


class Kitten(Cat):
    """
    This class represents a kitten.
    """

    def __init__(self, name: str, age: int) -> None:
        super().__init__(name=name, age=age, gender='Female')

    def make_sound(self) -> str:
        return 'Meow'

    def __repr__(self) -> str:
        return f'This is {self.name}. {self.name} is a {self.age} year old {self.gender} {self.__class__.__name__}'
