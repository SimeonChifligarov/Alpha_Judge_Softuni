class Shop:
    """
    This class represents a shop with a name and a list of items.
    """

    def __init__(self, shop_name: str, shop_items: list) -> None:
        self.name = shop_name
        self.items = shop_items

    def get_items_count(self) -> int:
        """
        This method returns how many items the shop has.

        Returns:
            int: The number of items in the shop
        """
        return len(self.items)

# if __name__ == '__main__':
#     shop_name_input = input()
#     shop_items_input = [el for el in input().split()]
#     store = Shop(shop_name=shop_name_input, shop_items=shop_items_input)
#     print(store.get_items_count())
