class Vehicle:
    """
    Represents a vehicle with a type, model, price, and ownership management.
    """

    def __init__(self, v_type: str, model: str, price: int) -> None:
        self.type = v_type
        self.model = model
        self.price = price
        self.owner = None

    def buy(self, money: int, owner: str) -> str:
        if self.owner is not None:
            return 'Car already sold'
        if money < self.price:
            return 'Sorry, not enough money'

        self.owner = owner
        change = money - self.price
        return f'Successfully bought a {self.type}. Change: {change:.2f}'

    def sell(self) -> str:
        if self.owner is None:
            return 'Vehicle has no owner'

        self.owner = None
        return ''

    def __repr__(self) -> str:
        return (
            f'{self.model} {self.type} is owned by: {self.owner}'
            if self.owner
            else f'{self.model} {self.type} is on sale: {self.price}'
        )

# if __name__ == '__main__':
#     vehicle_instance = Vehicle(type=input(), model=input(), price=int(input()))
#
#     result = vehicle_instance.buy(money=int(input()), owner=input())
#     if result:
#         print(result)
#
#     result = vehicle_instance.sell()
#     if result:
#         print(result)
#
#     print(vehicle_instance)
