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

    def __str__(self) -> str:
        return f'Glass with {self.content} ml out of {Glass.capacity} ml'

    def __repr__(self) -> str:
        return f'Glass(content={self.content!r})'

    # def __repr__(self) -> str:
    #     cls_name = self.__class__.__name__
    #     attrs = ', '.join(f'{k}={v!r}' for k, v in self.__dict__.items())
    #     return f'{cls_name}({attrs})'

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Glass):
            return self.content == other.content
        return NotImplemented

    def __gt__(self, other: object) -> bool:
        if isinstance(other, Glass):
            return self.content > other.content
        return NotImplemented

# if __name__ == '__main__':
#     glass_instance = Glass()
#     print(glass_instance.fill(ml=100))
#     print(glass_instance.fill(ml=200))
#     print(glass_instance.info())
#     print(glass_instance.empty())
#     print(glass_instance.info())
#     another_glass = Glass()
#     another_glass.fill(ml=150)
#     print(glass_instance == another_glass)
#     print(glass_instance > another_glass)
#     print(str(glass_instance))
#     print(repr(glass_instance))
