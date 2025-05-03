def grocery_store(**items: int) -> str:
    """
    This function sorts grocery items based on quantity, name length, and name.

    Args:
        items: Named arguments where keys are product names and values are quantities

    Returns:
        A string with sorted products and their quantities
    """
    sorted_items = sorted(
        items.items(),
        key=lambda x: (-x[1], -len(x[0]), x[0])
    )
    receipt = [f'{product}: {quantity}' for product, quantity in sorted_items]
    return '\n'.join(receipt)

# if __name__ == '__main__':
#     products = {
#         'Apples': 5,
#         'Bananas': 5,
#         'Cherries': 12,
#         'Blueberries': 5,
#     }
#     print(grocery_store(**products))
