class Shop:
    """This class helps you manage a shop with items and basic operations like add and remove."""

    def __init__(self, name: str, type_: str, capacity: int) -> None:
        self.name: str = name
        self.type: str = type_
        self.capacity: int = capacity
        self.items: dict[str, int] = {}

    @classmethod
    def small_shop(cls, name: str, type_: str) -> 'Shop':
        return cls(name, type_, 10)

    def add_item(self, item_name: str) -> str:
        if self.get_items_count() >= self.capacity:
            return 'Not enough capacity in the shop'
        if item_name not in self.items:
            self.items[item_name] = 0
        self.items[item_name] += 1
        return f'{item_name} added to the shop'

    def remove_item(self, item_name: str, amount: int) -> str:
        if item_name not in self.items or self.items[item_name] < amount:
            return f'Cannot remove {amount} {item_name}'
        self.items[item_name] -= amount
        if self.items[item_name] == 0:
            del self.items[item_name]
        return f'{amount} {item_name} removed from the shop'

    def __repr__(self) -> str:
        return f'{self.name} of type {self.type} with capacity {self.capacity}'

    # def __str__(self) -> str:
    #     return f'Shop: {self.name}, Type: {self.type}, Capacity: {self.capacity}, Items: {self.items}'

    def __len__(self) -> int:
        return self.get_items_count()

    def get_items_count(self) -> int:
        return sum(self.items.values())


if __name__ == '__main__':
    # fresh_shop = Shop(name='Fresh Shop', type_='Fruit and Veg', capacity=50)
    # small_shop = Shop.small_shop(name='Fashion Boutique', type_='Clothes')
    # print(fresh_shop)
    # print(small_shop)
    # print(fresh_shop.add_item(item_name='Bananas'))
    # print(fresh_shop.remove_item(item_name='Tomatoes', amount=2))
    # print(small_shop.add_item(item_name='Jeans'))
    # print(small_shop.add_item(item_name='Jeans'))
    # print(small_shop.remove_item(item_name='Jeans', amount=2))
    # print(small_shop.items)
    pass
