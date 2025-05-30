class Player:
    """
    This class is about a football player with sprint, dribble, passing, and shooting.

    Args:
        name (str): The name of the player.
        sprint (int): Points for sprint.
        dribble (int): Points for dribble.
        passing (int): Points for passing.
        shooting (int): Points for shooting.
    """

    def __init__(self, name: str, sprint: int, dribble: int, passing: int, shooting: int) -> None:
        self.__name = name
        self.__sprint = sprint
        self.__dribble = dribble
        self.__passing = passing
        self.__shooting = shooting

    @property
    def name(self) -> str:
        return self.__name

    def __str__(self) -> str:
        return f'Player: {self.__name}\nSprint: {self.__sprint}\nDribble: {self.__dribble}\nPassing: {self.__passing}\nShooting: {self.__shooting}'  # noqa


if __name__ == '__main__':
    pass
