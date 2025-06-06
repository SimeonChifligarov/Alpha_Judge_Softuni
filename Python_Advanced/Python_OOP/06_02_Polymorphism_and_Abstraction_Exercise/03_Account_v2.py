from typing import List, Any


class Account:
    """
    This class represents a bank account.

    Args:
        owner (str): The owner of the account.
        amount (int): The starting amount. Default is 0.
    """

    def __init__(self, owner: str, amount: int = 0) -> None:
        self.owner = owner
        self.amount = amount
        self._transactions: List[int] = []

    def handle_transaction(self, transaction_amount: int) -> str:
        """
        Handle a transaction and update the balance.

        Args:
            transaction_amount (int): The transaction amount.

        Returns:
            str: New balance message.

        Raises:
            ValueError: If the transaction would cause debt.
        """
        if self.balance + transaction_amount < 0:
            raise ValueError('sorry cannot go in debt!')
        self._transactions.append(transaction_amount)
        return f'New balance: {self.balance}'

    def add_transaction(self, amount: Any) -> None:
        """
        Add a transaction after checking type.

        Args:
            amount (Any): The transaction amount.

        Raises:
            ValueError: If the amount is not an int.
        """
        if not isinstance(amount, int):
            raise ValueError('please use int for amount')
        self._transactions.append(amount)

    @property
    def balance(self) -> int:
        """
        Get the current balance.

        Returns:
            int: The balance.
        """
        return self.amount + sum(self._transactions)

    @staticmethod
    def validate_transaction(account: 'Account', amount_to_add: int) -> str:
        """
        Validate and apply a transaction to an account.

        Args:
            account (Account): The account to validate for.
            amount_to_add (int): The transaction amount.

        Returns:
            str: New balance message.

        Raises:
            ValueError: If the transaction would cause debt.
        """
        if account.balance + amount_to_add < 0:
            raise ValueError('sorry cannot go in debt!')
        account._transactions.append(amount_to_add)
        return f'New balance: {account.balance}'

    def __str__(self) -> str:
        return f'Account of {self.owner} with starting amount: {self.amount}'

    def __repr__(self) -> str:
        return f'Account({self.owner}, {self.amount})'

    def __len__(self) -> int:
        return len(self._transactions)

    def __getitem__(self, item: int) -> int:
        return self._transactions[item]

    def __reversed__(self) -> List[int]:
        return list(reversed(self._transactions))

    def __add__(self, other: 'Account') -> 'Account':
        new_owner = f'{self.owner}&{other.owner}'
        new_amount = self.amount + other.amount
        new_account = Account(owner=new_owner, amount=new_amount)
        new_account._transactions = self._transactions + other._transactions
        return new_account

    def __gt__(self, other: 'Account') -> bool:
        return self.balance > other.balance

    def __ge__(self, other: 'Account') -> bool:
        return self.balance >= other.balance

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, Account):
            return False
        return self.balance == other.balance

    def __ne__(self, other: Any) -> bool:
        if not isinstance(other, Account):
            return False
        return not self.balance == other.balance

    def __lt__(self, other: 'Account') -> bool:
        return self.balance < other.balance

    def __le__(self, other: 'Account') -> bool:
        return self.balance <= other.balance


if __name__ == '__main__':
    # acc = Account(owner='bob', amount=10)
    # acc2 = Account(owner='john')
    # print(acc)
    # print(repr(acc))
    # acc.add_transaction(amount=20)
    # acc.add_transaction(amount=-20)
    # acc.add_transaction(amount=30)
    # print(acc.balance)
    # print(len(acc))
    # for transaction in acc:
    #     print(transaction)
    # print(acc[1])
    # print(list(reversed(acc)))
    # acc2.add_transaction(amount=10)
    # acc2.add_transaction(amount=60)
    # print(acc > acc2)
    # print(acc >= acc2)
    # print(acc < acc2)
    # print(acc <= acc2)
    # print(acc == acc2)
    # print(acc != acc2)
    # acc3 = acc + acc2
    # print(acc3)
    # print(acc3._transactions)
    pass
