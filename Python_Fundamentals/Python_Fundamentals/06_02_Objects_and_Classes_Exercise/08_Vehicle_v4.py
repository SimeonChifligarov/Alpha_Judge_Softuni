class Vehicle:
    def __init__(self, vehicle_type: str, model: str, price: int):
        """Initializes the vehicle with type, model, price, and sets the owner to None."""
        self.type = vehicle_type
        self.model = model
        self.price = price
        self.owner = None

    def buy(self, money: int, owner: str) -> str:
        """Handles vehicle purchase logic."""
        if self.owner is not None:
            return 'Car already sold'
        if money < self.price:
            return 'Sorry, not enough money'

        self.owner = owner
        change = money - self.price
        return f'Successfully bought a {self.type}. Change: {change:.2f}'

    def sell(self) -> str:
        """Handles selling the vehicle by resetting the owner."""
        if self.owner is None:
            return 'Vehicle has no owner'

        self.owner = None
        return 'Vehicle is now available for sale'

    def __repr__(self) -> str:
        """Returns a formatted string representation of the vehicle."""
        if self.owner:
            return f'{self.model} {self.type} is owned by: {self.owner}'
        return f'{self.model} {self.type} is on sale: {self.price}'
