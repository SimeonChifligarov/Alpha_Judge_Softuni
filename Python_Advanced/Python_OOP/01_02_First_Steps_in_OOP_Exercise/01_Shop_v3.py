class Shop:
    """
    This class is for a shop. It stores the name and a list of items.

    Args:
        name (str): The name of the shop
        items (list): A list of items in the shop
    """

    def __init__(self, name: str, items: list) -> None:
        self.name = name
        self.items = items

    def get_items_count(self) -> int:
        """
        This method gives the total number of items in the shop.

        Returns:
            int: Total count of items
        """
        return len(self.items)

    def __len__(self) -> int:
        return len(self.items)

    def __repr__(self) -> str:
        return f'Shop(name={self.name!r}, items={self.items!r})'

    def __str__(self) -> str:
        return f'{self.name} has {len(self.items)} items.'

# if __name__ == '__main__':
#     store_name = 'Book Haven'
#     store_items = ['book', 'pen', 'notebook']
#     shop_instance = Shop(name=store_name, items=store_items)
#     print(shop_instance.get_items_count())
#     print(len(shop_instance))
#     print(repr(shop_instance))
#     print(str(shop_instance))
