class Category:
    """This class creates a category to organize documents."""

    def __init__(self, category_id: int, category_name: str) -> None:
        self.id: int = category_id
        self.name: str = category_name

    def edit(self, new_name: str) -> None:
        self.name = new_name

    def __repr__(self) -> str:
        return f'Category {self.id}: {self.name}'


if __name__ == '__main__':
    # category_instance = Category(category_id=1, category_name='work')
    pass
