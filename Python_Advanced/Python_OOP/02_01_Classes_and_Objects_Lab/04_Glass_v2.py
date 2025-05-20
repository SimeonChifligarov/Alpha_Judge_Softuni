class Glass:
    """
    This class is for a glass. It starts empty and can be filled with liquid.

    Class Attributes:
        capacity (int): The total space in the glass in ml

    Instance Attributes:
        content (int): The current amount of liquid in the glass
    """

    capacity = 250

    def __init__(self) -> None:
        self.content = 0

    def fill(self, ml: int) -> str:
        """
        This method tries to fill the glass with a given amount.

        Args:
            ml (int): The amount of liquid to add

        Returns:
            str: Message about the result
        """
        if self.content + ml <= Glass.capacity:
            self.content += ml
            return f'Glass filled with {ml} ml'
        return f'Cannot add {ml} ml'

    def empty(self) -> str:
        """
        This method empties the glass.

        Returns:
            str: Confirmation that the glass is empty
        """
        self.content = 0
        return 'Glass is now empty'

    def info(self) -> str:
        """
        This method gives info about how much space is left.

        Returns:
            str: Remaining space in the glass
        """
        return f'{Glass.capacity - self.content} ml left'

# if __name__ == '__main__':
#     glass_instance = Glass()
#     print(glass_instance.fill(ml=100))
#     print(glass_instance.fill(ml=200))
#     print(glass_instance.info())
#     print(glass_instance.empty())
#     print(glass_instance.info())
