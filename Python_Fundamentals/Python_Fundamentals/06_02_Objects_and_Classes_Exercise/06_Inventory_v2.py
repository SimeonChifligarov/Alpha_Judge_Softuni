# Create a class Inventory. The __init__ method should accept only the capacity
# of the inventory. The capacity should be a private attribute (__capacity).
# You can read more about private attributes here. Each inventory should also
# have an attribute called items, where all the items will be stored.
# The class should also have 3 methods:
# •	add_item(item) - adds the item in the inventory if there is space for it.
# Otherwise, returns 'not enough room in the inventory'
# •	get_capacity() - returns the value of __capacity
# •	__repr__() - returns 'Items: {items}.\nCapacity left: {left_capacity}'.
# The items should be separated by ', '

class Inventory:
    def __init__(self, capacity):
        self.__capacity = capacity
        self.items = []

    def add_item(self, item):
        if self.__capacity <= len(self.items):
            return 'not enough room in the inventory'

        self.items.append(item)

    def get_capacity(self):
        return self.__capacity

    def _get_capacity_left(self):
        return self.__capacity - len(self.items)

    def __repr__(self):
        return f'Items: {", ".join(self.items)}.\nCapacity left: {self._get_capacity_left()}'

#
# inventory = Inventory(2)
# inventory.add_item('potion')
# inventory.add_item('sword')
# print(inventory.add_item('bottle'))
# print(inventory.get_capacity())
# print(inventory)
#
