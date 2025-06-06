from typing import List, Any


class Account:
    """
    This class represents a bank account.

    Args:
        owner (str): The owner of the account.
        amount (int): The starting amount of the account. Default is 0.
    """

    def __init__(self, owner: str, amount: int = 0) -> None:
        self.owner = owner
        self.amount = amount
        self._transactions: List[int] = []

    def handle_transaction(self, transaction_amount: int) -> str:
        """
        Handle a transaction and update the balance.

        Args:
            transaction_amount (int): The transaction amount to process.

        Returns:
            str: A message with the new balance.

        Raises:
            ValueError: If balance would go below zero.
        """
        if self.balance + transaction_amount < 0:
            raise ValueError('sorry cannot go in debt!')
        self._transactions.append(transaction_amount)
        return f'New balance: {self.balance}'

    def add_transaction(self, amount: Any) -> str:
        """
        Add a transaction after validating input.

        Args:
            amount (Any): The amount to add.

        Returns:
            str: A message with the new balance.

        Raises:
            ValueError: If amount is not an integer or would cause debt.
        """
        if not isinstance(amount, int):
            raise ValueError('please use int for amount')
        return self.handle_transaction(transaction_amount=amount)

    @property
    def balance(self) -> int:
        """
        Get the current balance.

        Returns:
            int: The current balance.
        """
        return self.amount + sum(self._transactions)

    def __str__(self) -> str:
        return f'Account of {self.owner} with starting amount: {self.amount}'

    def __repr__(self) -> str:
        return f'Account({self.owner}, {self.amount})'

    def __len__(self) -> int:
        return len(self._transactions)

    def __getitem__(self, index: int) -> int:
        return self._transactions[index]

    def __iter__(self) -> 'Account':
        self._index = 0
        return self

    def __next__(self) -> int:
        if self._index >= len(self._transactions):
            raise StopIteration
        result = self._transactions[self._index]
        self._index += 1
        return result

    def __reversed__(self) -> List[int]:
        return list(reversed(self._transactions))

    def __gt__(self, other: 'Account') -> bool:
        return self.balance > other.balance

    def __ge__(self, other: 'Account') -> bool:
        return self.balance >= other.balance

    def __lt__(self, other: 'Account') -> bool:
        return self.balance < other.balance

    def __le__(self, other: 'Account') -> bool:
        return self.balance <= other.balance

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, Account):
            return False
        return self.balance == other.balance

    def __ne__(self, other: Any) -> bool:
        if not isinstance(other, Account):
            return False
        return self.balance != other.balance

    def __add__(self, other: 'Account') -> 'Account':
        if not isinstance(other, Account):
            return NotImplemented
        new_owner = f'{self.owner}&{other.owner}'
        new_amount = self.amount + other.amount
        new_account = Account(owner=new_owner, amount=new_amount)
        new_account._transactions = self._transactions + other._transactions
        return new_account


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
