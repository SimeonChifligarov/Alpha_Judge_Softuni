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


if __name__ == '__main__':
    # fruit_name_input = input()
    # expiration_date_input = input()
    # fruit_item = Fruit(name=fruit_name_input, expiration_date=expiration_date_input)
    pass
