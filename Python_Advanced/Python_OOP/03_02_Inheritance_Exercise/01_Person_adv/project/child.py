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

    def __str__(self) -> str:
        return f'Child(name={self.name}, age={self.age})'

    def __repr__(self) -> str:
        return f'Child(name={self.name}, age={self.age})'

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Child):
            return False
        return self.name == other.name and self.age == other.age

    def __hash__(self) -> int:
        return hash((self.name, self.age))


if __name__ == '__main__':
    # child_instance = Child(name='John', age=5)
    # print(child_instance)
    pass
