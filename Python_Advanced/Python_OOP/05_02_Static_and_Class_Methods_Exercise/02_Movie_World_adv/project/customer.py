class Customer:
    """This class helps to create a customer who can rent DVDs."""

    def __init__(self, name: str, age: int, customer_id: int) -> None:
        self.name: str = name
        self.age: int = age
        self.id: int = customer_id
        self.rented_dvds: list = []

    def __repr__(self) -> str:
        rented_dvds_names: str = ', '.join(dvd.name for dvd in self.rented_dvds)
        return f'{self.id}: {self.name} of age {self.age} has {len(self.rented_dvds)} rented DVD\'s ({rented_dvds_names})'


if __name__ == '__main__':
    # customer_instance = Customer(name='John', age=16, customer_id=1)
    pass
