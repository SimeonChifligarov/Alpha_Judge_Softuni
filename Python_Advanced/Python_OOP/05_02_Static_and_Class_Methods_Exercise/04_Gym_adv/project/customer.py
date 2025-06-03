class Customer:
    """
    This class represents a customer who signs up for the gym.

    Args:
        name (str): The name of the customer.
        address (str): The address of the customer.
        email (str): The email address of the customer.
    """

    id_counter: int = 1

    def __init__(self, name: str, address: str, email: str) -> None:
        self.name = name
        self.address = address
        self.email = email
        self.id = Customer.id_counter
        Customer.id_counter += 1

    @staticmethod
    def get_next_id() -> int:
        """
        Get the id that will be given to the next customer.

        Returns:
            int: The next id number.
        """
        return Customer.id_counter

    def __repr__(self) -> str:
        return f'Customer <{self.id}> {self.name}; Address: {self.address}; Email: {self.email}'
