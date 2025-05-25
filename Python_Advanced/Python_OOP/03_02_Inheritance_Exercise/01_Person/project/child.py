from project.person import Person


class Child(Person):
    """
    This class is about a child who has a name and age.

    Args:
        name (str): The name of the child.
        age (int): The age of the child.
    """

    def __init__(self, name: str, age: int) -> None:
        super().__init__(name=name, age=age)


if __name__ == '__main__':
    # child_instance = Child(name='John', age=5)
    # print(child_instance)
    pass
