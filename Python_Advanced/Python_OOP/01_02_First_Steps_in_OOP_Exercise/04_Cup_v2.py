class Cup:
    """
    This class is for a cup. It has a size and how much liquid it holds.

    Args:
        size (int): The total capacity of the cup
        quantity (int): The current amount of liquid in the cup
    """

    def __init__(self, size: int, quantity: int) -> None:
        self.size = size
        self.quantity = quantity

    def fill(self, quantity: int) -> None:
        """
        This method tries to add more liquid to the cup. It only adds if there is enough space.

        Args:
            quantity (int): The amount of liquid to add
        """
        if self.quantity + quantity <= self.size:
            self.quantity += quantity

    def status(self) -> int:
        """
        This method shows how much more liquid the cup can take.

        Returns:
            int: Free space left
        """
        return self.size - self.quantity

# if __name__ == '__main__':
#     cup_size = 250
#     current_quantity = 100
#     cup_instance = Cup(size=cup_size, quantity=current_quantity)
#     cup_instance.fill(quantity=80)
#     print(cup_instance.status())
#     cup_instance.fill(quantity=100)
#     print(cup_instance.status())
