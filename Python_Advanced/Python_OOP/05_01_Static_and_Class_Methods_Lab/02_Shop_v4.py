class Shop:
    """This class helps to create a shop, add and remove items, and handle shop capacity."""

    SMALL_SHOP_CAPACITY: int = 10
    NOT_ENOUGH_CAPACITY_MESSAGE: str = 'Not enough capacity in the shop'

    def __init__(self, shop_name: str, shop_type: str, shop_capacity: int) -> None:
        self.name: str = shop_name
        self.type: str = shop_type
        self.capacity: int = shop_capacity
        self.items: dict[str, int] = {}

    @classmethod
    def small_shop(cls, shop_name: str, shop_type: str) -> 'Shop':
        return cls(shop_name, shop_type, cls.SMALL_SHOP_CAPACITY)

    def add_item(self, item_name: str) -> str:
        if self.__get_current_quantity() >= self.capacity:
            return self.NOT_ENOUGH_CAPACITY_MESSAGE

        if item_name not in self.items:
            self.items[item_name] = 0
        self.items[item_name] += 1
        return self.__get_success_add_message(item_name=item_name)

    def remove_item(self, item_name: str, remove_count: int) -> str:
        if item_name not in self.items or self.items[item_name] < remove_count:
            return self.__get_fail_remove_message(item_name=item_name, amount=remove_count)

        self.items[item_name] -= remove_count
        if self.items[item_name] == 0:
            del self.items[item_name]
        return self.__get_success_remove_message(item_name=item_name, amount=remove_count)

    def __get_current_quantity(self) -> int:
        return sum(self.items.values())

    @staticmethod
    def __get_success_add_message(item_name: str) -> str:
        return f'{item_name} added to the shop'

    @staticmethod
    def __get_fail_remove_message(item_name: str, amount: int) -> str:
        return f'Cannot remove {amount} {item_name}'

    @staticmethod
    def __get_success_remove_message(item_name: str, amount: int) -> str:
        return f'{amount} {item_name} removed from the shop'

    def __repr__(self) -> str:
        return f'{self.name} of type {self.type} with capacity {self.capacity}'


if __name__ == '__main__':
    # fresh_shop_instance = Shop(shop_name='Fresh Shop', shop_type='Fruit and Veg', shop_capacity=50)
    # small_shop_instance = Shop.small_shop(shop_name='Fashion Boutique', shop_type='Clothes')
    # print(fresh_shop_instance)
    # print(small_shop_instance)
    # print(fresh_shop_instance.add_item(item_name='Bananas'))
    # print(fresh_shop_instance.remove_item(item_name='Tomatoes', remove_count=2))
    # print(small_shop_instance.add_item(item_name='Jeans'))
    # print(small_shop_instance.add_item(item_name='Jeans'))
    # print(small_shop_instance.remove_item(item_name='Jeans', remove_count=2))
    # print(small_shop_instance.items)
    pass
