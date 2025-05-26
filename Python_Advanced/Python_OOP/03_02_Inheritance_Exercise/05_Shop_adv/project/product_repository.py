from project.product import Product


class ProductRepository:
    """
    This class is about a product repository that keeps products.

    Attributes:
        products (list): A list of products.
    """

    def __init__(self) -> None:
        self.products: list[Product] = []

    def add(self, product: Product) -> None:
        existing_product = self.find(product_name=product.name)
        if existing_product:
            existing_product.increase(quantity=product.quantity)
        else:
            self.products.append(product)

    def find(self, product_name: str) -> Product | None:
        for product in self.products:
            if product.name == product_name:
                return product
        return None

    def remove(self, product_name: str) -> None:
        product_to_remove = self.find(product_name=product_name)
        if product_to_remove:
            self.products.remove(product_to_remove)

    def __repr__(self) -> str:
        return '\n'.join(f'{product.name}: {product.quantity}' for product in self.products)


if __name__ == '__main__':
    # repo_instance = ProductRepository()
    pass
