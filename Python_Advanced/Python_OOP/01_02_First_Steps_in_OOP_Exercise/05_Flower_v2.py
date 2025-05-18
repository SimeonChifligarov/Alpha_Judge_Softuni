class Flower:
    """
    This class is for a flower. It needs some water to become happy.

    Args:
        name (str): The name of the flower
        water_requirements (int): How much water the flower needs to be happy
    """

    def __init__(self, name: str, water_requirements: int) -> None:
        self.name = name
        self.water_requirements = water_requirements
        self.is_happy = False

    def water(self, quantity: int) -> None:
        """
        This method waters the flower. If enough water is given, it becomes happy.

        Args:
            quantity (int): The amount of water given
        """
        if quantity >= self.water_requirements:
            self.is_happy = True

    def status(self) -> str:
        """
        This method says if the flower is happy or not.

        Returns:
            str: The current mood of the flower
        """
        return f'{self.name} is happy' if self.is_happy else f'{self.name} is not happy'

# if __name__ == '__main__':
#     flower_name = 'Rose'
#     required_water = 50
#     flower_instance = Flower(name=flower_name, water_requirements=required_water)
#     flower_instance.water(quantity=30)
#     print(flower_instance.status())
#     flower_instance.water(quantity=60)
#     print(flower_instance.status())
