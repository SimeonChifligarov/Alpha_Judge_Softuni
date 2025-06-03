class ExercisePlan:
    """
    This class represents an exercise plan.

    Args:
        trainer_id (int): The trainer id assigned.
        equipment_id (int): The equipment id assigned.
        duration (int): Duration in minutes.
    """

    id_counter: int = 1

    def __init__(self, trainer_id: int, equipment_id: int, duration: int) -> None:
        self.trainer_id = trainer_id
        self.equipment_id = equipment_id
        self.duration = duration
        self.id = ExercisePlan.id_counter
        ExercisePlan.id_counter += 1

    @classmethod
    def from_hours(cls, trainer_id: int, equipment_id: int, hours: int) -> 'ExercisePlan':
        """
        Create a new plan by giving hours instead of minutes.

        Args:
            trainer_id (int): The trainer id.
            equipment_id (int): The equipment id.
            hours (int): The duration in hours.

        Returns:
            ExercisePlan: New exercise plan created.
        """
        return cls(trainer_id, equipment_id, hours * 60)

    @staticmethod
    def get_next_id() -> int:
        """
        Get the id that will be given to the next plan.

        Returns:
            int: The next id number.
        """
        return ExercisePlan.id_counter

    def __repr__(self) -> str:
        return f'Plan <{self.id}> with duration {self.duration} minutes'
