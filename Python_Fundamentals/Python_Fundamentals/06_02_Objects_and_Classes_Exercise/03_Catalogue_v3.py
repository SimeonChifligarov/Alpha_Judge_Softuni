class Catalogue:
    def __init__(self, name: str):
        """Initializes the catalogue with a given name and an empty product list."""
        self.name = name
        self.products = []

    def add_product(self, product_name: str):
        """Adds a product to the catalogue list."""
        self.products.append(product_name)

    def get_by_letter(self, first_letter: str) -> list:
        """Returns a list of products that start with the given letter."""
        return [product for product in self.products if product.startswith(first_letter)]

    def __repr__(self) -> str:
        """Returns a formatted string representation of the catalogue sorted alphabetically."""
        sorted_products = sorted(self.products)
        return f'Items in the {self.name} catalogue:\n' + '\n'.join(sorted_products)
