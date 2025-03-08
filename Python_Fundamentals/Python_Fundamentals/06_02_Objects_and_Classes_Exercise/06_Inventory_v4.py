class Inventory:
    def __init__(self, capacity: int):
        """Initializes the inventory with a private capacity and an empty list of items."""
        self.__capacity = capacity
        self.items = []

    def add_item(self, item: str) -> str:
        """Adds an item to the inventory if there is available space."""
        if len(self.items) < self.__capacity:
            self.items.append(item)
        else:
            return 'not enough room in the inventory'

    def get_capacity(self) -> int:
        """Returns the total capacity of the inventory."""
        return self.__capacity

    def __repr__(self) -> str:
        """Returns a formatted string representation of the inventory."""
        remaining_capacity = self.__capacity - len(self.items)
        return f'Items: {", ".join(self.items)}.\nCapacity left: {remaining_capacity}'
