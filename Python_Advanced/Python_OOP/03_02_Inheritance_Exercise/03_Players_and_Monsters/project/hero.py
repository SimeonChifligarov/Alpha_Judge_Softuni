class Hero:
    """
    This class is about a hero who has a username and a level.

    Args:
        username (str): The username of the hero.
        level (int): The level of the hero.
    """

    def __init__(self, username: str, level: int) -> None:
        self.username = username
        self.level = level

    def __str__(self) -> str:
        return f'{self.username} of type {type(self).__name__} has level {self.level}'


if __name__ == '__main__':
    # hero_instance = Hero(username='Arthur', level=10)
    # print(hero_instance)
    pass
