def grocery_store(**products: int) -> str:
    """
    This function orders products by quantity, name length, and name itself.

    Args:
        products: Items with their names and quantities

    Returns:
        A string showing all items sorted nicely
    """
    entries = [(name, quantity) for name, quantity in products.items()]

    # TODO: suboptimal - sorting in 3 steps
    entries.sort(key=lambda item: item[0])
    entries.sort(key=lambda item: len(item[0]), reverse=True)
    entries.sort(key=lambda item: item[1], reverse=True)
    final_receipt = '\n'.join([f'{name}: {quantity}' for name, quantity in entries])
    return final_receipt

# if __name__ == '__main__':
#     store_items = {
#         'Bread': 7,
#         'Milk': 10,
#         'Cheese': 10,
#         'Butter': 5,
#     }
#     print(grocery_store(**store_items))
