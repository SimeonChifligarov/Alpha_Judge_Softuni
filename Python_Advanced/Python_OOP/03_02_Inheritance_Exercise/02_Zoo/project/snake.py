from project.reptile import Reptile


class Snake(Reptile):
    """
    This class is about a snake that is a kind of reptile.

    Args:
        name (str): The name of the snake.
    """

    def __init__(self, name: str) -> None:
        super().__init__(name=name)


if __name__ == '__main__':
    # snake_instance = Snake(name='Slither')
    # print(snake_instance.name)
    pass
