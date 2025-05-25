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

    def __repr__(self) -> str:
        return f'Hero(username={self.username}, level={self.level})'

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Hero):
            return False
        return self.username == other.username and self.level == other.level

    def __hash__(self) -> int:
        return hash((self.username, self.level))


if __name__ == '__main__':
    # hero_instance = Hero(username='Arthur', level=10)
    # print(hero_instance)
    pass
