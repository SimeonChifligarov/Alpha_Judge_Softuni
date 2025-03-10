def create_product_dict(products: list[str]) -> dict[str, int]:
    """Creates a dictionary from a list of products and their quantities."""
    return {products[i]: int(products[i + 1]) for i in range(0, len(products), 2)}


def check_products_availability(stock: dict[str, int], queries: list[str]) -> list[str]:
    """Checks if queried products are in stock and returns appropriate messages."""
    return [
        f'We have {stock[item]} of {item} left' if item in stock
        else f'Sorry, we don\'t have {item}'
        for item in queries
    ]


if __name__ == '__main__':
    stock_input = input().split()
    query_input = input().split()
    product_stock = create_product_dict(products=stock_input)
    results = check_products_availability(stock=product_stock, queries=query_input)
    print('\n'.join(results))
