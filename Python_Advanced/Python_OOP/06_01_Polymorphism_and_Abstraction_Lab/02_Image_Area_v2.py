class ImageArea:
    """
    This class represents an image area using width and height.

    Args:
        width (int): The width of the image.
        height (int): The height of the image.
    """

    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height

    def get_area(self) -> int:
        """
        Get the area of the image.

        Returns:
            int: The area of the image.
        """
        return self.width * self.height

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, ImageArea):
            return NotImplemented
        return self.get_area() == other.get_area()

    def __ne__(self, other: object) -> bool:
        if not isinstance(other, ImageArea):
            return NotImplemented
        return self.get_area() != other.get_area()

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, ImageArea):
            return NotImplemented
        return self.get_area() < other.get_area()

    def __le__(self, other: object) -> bool:
        if not isinstance(other, ImageArea):
            return NotImplemented
        return self.get_area() <= other.get_area()

    def __gt__(self, other: object) -> bool:
        if not isinstance(other, ImageArea):
            return NotImplemented
        return self.get_area() > other.get_area()

    def __ge__(self, other: object) -> bool:
        if not isinstance(other, ImageArea):
            return NotImplemented
        return self.get_area() >= other.get_area()


if __name__ == '__main__':
    # image_area_1 = ImageArea(width=7, height=10)
    # image_area_2 = ImageArea(width=35, height=2)
    # image_area_3 = ImageArea(width=8, height=9)
    #
    # print(image_area_1 == image_area_2)
    # print(image_area_1 != image_area_3)
    #
    # image_area_1 = ImageArea(width=7, height=10)
    # image_area_2 = ImageArea(width=35, height=2)
    # image_area_3 = ImageArea(width=8, height=9)
    #
    # print(image_area_1 != image_area_2)
    # print(image_area_1 >= image_area_3)
    #
    # image_area_1 = ImageArea(width=7, height=10)
    # image_area_2 = ImageArea(width=35, height=2)
    # image_area_3 = ImageArea(width=8, height=9)
    #
    # print(image_area_1 <= image_area_2)
    # print(image_area_1 < image_area_3)
    pass
