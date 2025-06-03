class Equipment:
    """
    This class represents gym equipment.

    Args:
        name (str): The name of the equipment.
    """

    id_counter: int = 1

    def __init__(self, name: str) -> None:
        self.name = name
        self.id = Equipment.id_counter
        Equipment.id_counter += 1

    @staticmethod
    def get_next_id() -> int:
        """
        Get the id that will be given to the next equipment.

        Returns:
            int: The next id number.
        """
        return Equipment.id_counter

    def __repr__(self) -> str:
        return f'Equipment <{self.id}> {self.name}'
