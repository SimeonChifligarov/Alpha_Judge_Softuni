class Trainer:
    """
    This class represents a trainer who works at the gym.

    Args:
        name (str): The name of the trainer.
    """

    id_counter: int = 1

    def __init__(self, name: str) -> None:
        self.name = name
        self.id = Trainer.id_counter
        Trainer.id_counter += 1

    @staticmethod
    def get_next_id() -> int:
        """
        Get the id that will be given to the next trainer.

        Returns:
            int: The next id number.
        """
        return Trainer.id_counter

    def __repr__(self) -> str:
        return f'Trainer <{self.id}> {self.name}'
