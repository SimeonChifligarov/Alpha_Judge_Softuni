class Mammal:
    """
    This class is about a mammal that has a name, type, and sound.

    Args:
        name (str): The name of the mammal.
        type (str): The type of the mammal.
        sound (str): The sound the mammal makes.
    """

    __kingdom: str = 'animals'

    def __init__(self, name: str, type: str, sound: str) -> None:
        self.name = name
        self.type = type
        self.sound = sound

    def make_sound(self) -> str:
        return f'{self.name} makes {self.sound}'

    def get_kingdom(self) -> str:
        return self.__kingdom

    def info(self) -> str:
        return f'{self.name} is of type {self.type}'


if __name__ == '__main__':
    # mammal_instance = Mammal(name='Dog', type='Domestic', sound='Bark')
    # print(mammal_instance.make_sound())
    # print(mammal_instance.get_kingdom())
    # print(mammal_instance.info())
    pass
