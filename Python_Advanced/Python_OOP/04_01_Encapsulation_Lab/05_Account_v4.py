class Account:
    """
    This class is about a bank account with an id, balance, and pin.

    Args:
        acc_id (int): The id of the account.
        balance (int): The balance of the account.
        pin (int): The security pin of the account.
    """

    def __init__(self, acc_id: int, balance: int, pin: int) -> None:
        self.__id = acc_id
        self.balance = balance
        self.__pin = pin

    def get_id(self, pin: int) -> int | str:
        if pin != self.__pin:
            return self.__get_wrong_pin_message()
        return self.__id

    def change_pin(self, old_pin: int, new_pin: int) -> str:
        if old_pin != self.__pin:
            return self.__get_wrong_pin_message()
        self.__pin = new_pin
        return self.__get_successful_change_pin_message()

    @staticmethod
    def __get_wrong_pin_message() -> str:
        return 'Wrong pin'

    @staticmethod
    def __get_successful_change_pin_message() -> str:
        return 'Pin changed'

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
    # account_instance = Account(acc_id=8827312, balance=100, pin=3421)
    # print(account_instance.get_id(pin=1111))
    # print(account_instance.get_id(pin=3421))
    # print(account_instance.balance)
    # print(account_instance.change_pin(old_pin=2212, new_pin=4321))
    # print(account_instance.change_pin(old_pin=3421, new_pin=1234))
    pass
