class Person:
    """
    This class is about a person who has a private name and a private age.

    Args:
        name (str): The name of the person.
        age (int): The age of the person.
    """

    def __init__(self, name: str, age: int) -> None:
        self.__name = name
        self.__age = age

    def get_name(self) -> str:
        return self.__name

    def get_age(self) -> int:
        return self.__age


if __name__ == '__main__':
    # person_instance = Person(name='George', age=32)
    # print(person_instance.get_name())
    # print(person_instance.get_age())
    pass
