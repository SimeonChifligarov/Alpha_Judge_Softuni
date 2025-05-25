class Person:
    """
    This class is about a person who has a name and age.

    Args:
        name (str): The name of the person.
        age (int): The age of the person.
    """

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def __str__(self) -> str:
        return f'Person(name={self.name}, age={self.age})'

    def __repr__(self) -> str:
        return f'Person(name={self.name}, age={self.age})'

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Person):
            return False
        return self.name == other.name and self.age == other.age

    def __hash__(self) -> int:
        return hash((self.name, self.age))


if __name__ == '__main__':
    # person_instance = Person(name='Peter', age=25)
    # print(person_instance.name)
    # print(person_instance.age)
    pass
