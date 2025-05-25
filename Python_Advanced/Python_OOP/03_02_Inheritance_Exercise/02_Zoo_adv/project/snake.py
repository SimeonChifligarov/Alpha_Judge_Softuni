from project.reptile import Reptile


class Snake(Reptile):
    """
    This class is about a snake that is a kind of reptile.

    Args:
        name (str): The name of the snake.
    """

    def __init__(self, name: str) -> None:
        super().__init__(name=name)

    def __str__(self) -> str:
        return f'Snake(name={self.name})'

    def __repr__(self) -> str:
        return f'Snake(name={self.name})'

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Snake):
            return False
        return self.name == other.name

    def __hash__(self) -> int:
        return hash(self.name)


if __name__ == '__main__':
    # snake_instance = Snake(name='Slither')
    # print(snake_instance.name)
    pass
