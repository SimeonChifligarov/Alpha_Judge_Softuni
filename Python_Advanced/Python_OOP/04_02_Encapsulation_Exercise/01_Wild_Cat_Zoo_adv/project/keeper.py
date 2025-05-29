from project.worker import Worker


class Keeper(Worker):
    """
    This class is about a keeper at the zoo.
    """

    def __init__(self, name: str, age: int, salary: int) -> None:
        super().__init__(name=name, age=age, salary=salary)


if __name__ == '__main__':
    pass
