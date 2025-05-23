from project.food import Food


class Fruit(Food):
    """
    This class is about a fruit that has a name and an expiration date.

    Args:
        name (str): The name of the fruit.
        expiration_date (str): The date when the fruit expires.
    """

    def __init__(self, name: str, expiration_date: str) -> None:
        super().__init__(expiration_date=expiration_date)
        self.name = name

    def __str__(self) -> str:
        return f'Fruit(name={self.name}, expiration_date={self.expiration_date})'

    def __repr__(self) -> str:
        return f'Fruit(name={self.name}, expiration_date={self.expiration_date})'

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Fruit):
            return False
        return self.name == other.name and self.expiration_date == other.expiration_date

    def __hash__(self) -> int:
        return hash((self.name, self.expiration_date))


# if __name__ == '__main__':
    # fruit_name_input = input()
    # expiration_date_input = input()
    # fruit_item = Fruit(name=fruit_name_input, expiration_date=expiration_date_input)
    # print(fruit_item)
