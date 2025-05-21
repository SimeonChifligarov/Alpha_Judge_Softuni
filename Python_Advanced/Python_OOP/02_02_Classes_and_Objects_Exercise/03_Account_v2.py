class Account:
    """
    This class is for a bank account. It stores an ID, name, and balance.

    Args:
        id (int): The account ID
        name (str): The owner's name
        balance (int, optional): The starting balance. Defaults to 0.
    """

    def __init__(self, id: int, name: str, balance: int = 0) -> None:
        self.id = id
        self.name = name
        self.balance = balance

    def credit(self, amount: int) -> int:
        """
        This method adds money to the account.

        Args:
            amount (int): How much to add

        Returns:
            int: New balance
        """
        self.balance += amount
        return self.balance

    def debit(self, amount: int) -> int | str:
        """
        This method removes money from the account if there is enough.

        Args:
            amount (int): How much to remove

        Returns:
            int | str: New balance or error message
        """
        if amount <= self.balance:
            self.balance -= amount
            return self.balance
        return 'Amount exceeded balance'

    def info(self) -> str:
        """
        This method shows account information.

        Returns:
            str: User and balance info
        """
        return f'User {self.name} with account {self.id} has {self.balance} balance'

# if __name__ == '__main__':
#     account_id = 101
#     account_holder = 'Alice'
#     account_instance = Account(id=account_id, name=account_holder)
#     print(account_instance.credit(amount=200))
#     print(account_instance.debit(amount=50))
#     print(account_instance.debit(amount=300))
#     print(account_instance.info())
