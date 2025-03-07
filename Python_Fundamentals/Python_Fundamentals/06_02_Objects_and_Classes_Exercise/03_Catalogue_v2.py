class Catalogue:
    """
    Represents a product catalogue with methods to add products, filter by letter, and display sorted items.
    """

    def __init__(self, name: str) -> None:
        self.name = name
        self.products = []

    def add_product(self, product_name: str) -> None:
        self.products.append(product_name)

    def get_by_letter(self, first_letter: str) -> list[str]:
        return [product for product in self.products if product.startswith(first_letter)]

    def __repr__(self) -> str:
        sorted_products = '\n'.join(sorted(self.products))
        return f'Items in the {self.name} catalogue:\n{sorted_products}'

# if __name__ == '__main__':
#     catalogue_instance = Catalogue(name=input())
#
#     for _ in range(int(input())):
#         catalogue_instance.add_product(product_name=input())
#
#     print(catalogue_instance.get_by_letter(first_letter=input()))
#     print(catalogue_instance)
