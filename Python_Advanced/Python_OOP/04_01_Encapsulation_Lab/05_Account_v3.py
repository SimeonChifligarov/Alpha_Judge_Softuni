class Account:
    """
    This class is about a bank account with an id, balance, and pin.

    Args:
        id (int): The id of the account.
        balance (int): The balance of the account.
        pin (int): The security pin of the account.
    """

    def __init__(self, id: int, balance: int, pin: int) -> None:
        self.__id = id
        self.balance = balance
        self.__pin = pin

    def get_id(self, pin: int) -> int | str:
        if pin == self.__pin:
            return self.__id
        return 'Wrong pin'

    def change_pin(self, old_pin: int, new_pin: int) -> str:
        if old_pin == self.__pin:
            self.__pin = new_pin
            return 'Pin changed'
        return 'Wrong pin'

    def __str__(self) -> str:
        return f'Account(id=PRIVATE, balance={self.balance}, pin=PRIVATE)'

    def __repr__(self) -> str:
        return f'Account(id=PRIVATE, balance={self.balance}, pin=PRIVATE)'

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Account):
            return False
        return self.balance == other.balance

    def __hash__(self) -> int:
        return hash(self.balance)


if __name__ == '__main__':
    # account_instance = Account(id=8827312, balance=100, pin=3421)
    # print(account_instance.get_id(pin=1111))
    # print(account_instance.get_id(pin=3421))
    # print(account_instance.balance)
    # print(account_instance.change_pin(old_pin=2212, new_pin=4321))
    # print(account_instance.change_pin(old_pin=3421, new_pin=1234))
    pass
