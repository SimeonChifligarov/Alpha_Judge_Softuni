class Inventory:
    """
    Represents an inventory with a fixed capacity for storing items.
    """

    def __init__(self, capacity: int) -> None:
        self.__capacity = capacity
        self.items = []

    def add_item(self, item: str) -> str:
        if len(self.items) >= self.__capacity:
            return 'not enough room in the inventory'

        self.items.append(item)
        return ''

    def get_capacity(self) -> int:
        return self.__capacity

    def _get_capacity_left(self) -> int:
        return self.__capacity - len(self.items)

    def __repr__(self) -> str:
        return f'Items: {", ".join(self.items)}.\nCapacity left: {self._get_capacity_left()}'

# if __name__ == '__main__':
#     inventory_instance = Inventory(capacity=int(input()))
#
#     for _ in range(int(input())):
#         result = inventory_instance.add_item(item=input())
#         if result:
#             print(result)
#
#     print(inventory_instance)
