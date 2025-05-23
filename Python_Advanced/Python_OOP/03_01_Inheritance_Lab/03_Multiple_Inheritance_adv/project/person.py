class Person:
    """
    This class is about a person that can sleep.

    Methods:
        sleep(): Says that the person is sleeping.
    """

    # def sleep(self) -> str:
    #     return 'sleeping...'

    @staticmethod
    def sleep() -> str:
        return 'sleeping...'

    def __str__(self) -> str:
        return 'Person()'

    def __repr__(self) -> str:
        return 'Person()'

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Person)

    def __hash__(self) -> int:
        return hash('Person')


if __name__ == '__main__':
    # person_instance = Person()
    # print(person_instance.sleep())
    pass
