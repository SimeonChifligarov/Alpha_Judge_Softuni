class Storage:
    """
    Represents a storage system with a fixed capacity for storing products.
    """

    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.storage = []

    def add_product(self, product: str) -> None:
        if len(self.storage) < self.capacity:
            self.storage.append(product)

    def get_products(self) -> list[str]:
        return self.storage

# if __name__ == '__main__':
#     storage_instance = Storage(capacity=int(input()))
#     for _ in range(int(input())):
#         storage_instance.add_product(product=input())
#
#     print(storage_instance.get_products())
