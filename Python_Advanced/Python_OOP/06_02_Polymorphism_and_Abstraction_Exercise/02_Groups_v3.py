from typing import List, Iterator, Any


class Person:
    """
    This class represents a person with a name and a surname.

    Args:
        name (str): The first name of the person.
        surname (str): The surname of the person.
    """

    def __init__(self, name: str, surname: str) -> None:
        self.name = name
        self.surname = surname

    def __str__(self) -> str:
        return f'{self.name} {self.surname}'

    def __repr__(self) -> str:
        return f'Person(name={self.name}, surname={self.surname})'

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, Person):
            return False
        return self.name == other.name and self.surname == other.surname

    def __hash__(self) -> int:
        return hash((self.name, self.surname))

    def __add__(self, other: 'Person') -> 'Person':
        if not isinstance(other, Person):
            return NotImplemented
        return Person(name=self.name, surname=other.surname)


class Group:
    """
    This class represents a group of people.

    Args:
        name (str): The name of the group.
        people (List[Person]): The list of people in the group.
    """

    def __init__(self, name: str, people: List[Person]) -> None:
        self.name = name
        self.people = people

    def __len__(self) -> int:
        return len(self.people)

    def __add__(self, other: 'Group') -> 'Group':
        if not isinstance(other, Group):
            return NotImplemented
        new_name = f'{self.name} {other.name}'
        new_people = self.people + other.people
        return Group(name=new_name, people=new_people)

    def __str__(self) -> str:
        members = ', '.join(str(person) for person in self.people)
        return f'Group {self.name} with members {members}'

    def __repr__(self) -> str:
        return f'Group(name={self.name}, people={self.people})'

    def __getitem__(self, index: int) -> str:
        person = self.people[index]
        return f'Person {index}: {person}'

    def __iter__(self) -> Iterator[str]:
        self._index = 0
        return self

    def __next__(self) -> str:
        if self._index >= len(self.people):
            raise StopIteration
        result = f'Person {self._index}: {self.people[self._index]}'
        self._index += 1
        return result

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, Group):
            return False
        return self.name == other.name and self.people == other.people

    def __contains__(self, person: Any) -> bool:
        return person in self.people

    def __hash__(self) -> int:
        return hash((self.name, tuple(self.people)))


if __name__ == '__main__':
    # p0 = Person(name='Aliko', surname='Dangote')
    # p1 = Person(name='Bill', surname='Gates')
    # p2 = Person(name='Warren', surname='Buffet')
    # p3 = Person(name='Elon', surname='Musk')
    # p4 = p2 + p3
    #
    # first_group = Group(name='__VIP__', people=[p0, p1, p2])
    # second_group = Group(name='Special', people=[p3, p4])
    # third_group = first_group + second_group
    #
    # print(len(first_group))
    # print(second_group)
    # print(third_group[0])
    #
    # for person in third_group:
    #     print(person)
    pass
