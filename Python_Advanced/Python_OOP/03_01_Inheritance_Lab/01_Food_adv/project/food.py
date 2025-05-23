class Food:
    """
    This class is about a food item and when it expires.

    Args:
        expiration_date (str): The date when the food expires.
    """

    def __init__(self, expiration_date: str) -> None:
        self.expiration_date = expiration_date

    def __str__(self) -> str:
        return f'Food(expiration_date={self.expiration_date})'

    def __repr__(self) -> str:
        return f'Food(expiration_date={self.expiration_date})'

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Food):
            return False
        return self.expiration_date == other.expiration_date

    def __hash__(self) -> int:
        return hash(self.expiration_date)


# if __name__ == '__main__':
    # expiration_date_input = input()
    # food_item = Food(expiration_date=expiration_date_input)
    # print(food_item)
