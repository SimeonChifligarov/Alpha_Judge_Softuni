class Storage:
    def __init__(self, capacity: int):
        """Initializes the storage with a given capacity and an empty product list."""
        self.capacity = capacity
        self.storage = []

    def add_product(self, product: str):
        """Adds a product to storage if there is available capacity."""
        if len(self.storage) < self.capacity:
            self.storage.append(product)

    def get_products(self) -> list:
        """Returns the list of stored products."""
        return self.storage
