def create_product_dict(products: list[str]) -> dict[str, int]:
    """Creates a dictionary from a list of products and their quantities."""
    return {products[i]: int(products[i + 1]) for i in range(0, len(products), 2)}


def check_products_availability(stock: dict[str, int], queries: list[str]) -> None:
    """Checks if queried products are in stock and prints the appropriate message."""
    for item in queries:
        if item in stock:
            print(f'We have {stock[item]} of {item} left')
        else:
            print(f'Sorry, we don\'t have {item}')


if __name__ == '__main__':
    stock_input = input().split()
    query_input = input().split()
    product_stock = create_product_dict(products=stock_input)
    check_products_availability(stock=product_stock, queries=query_input)
