class Subscription:
    """
    This class represents a subscription to the gym.

    Args:
        date (str): The date of the subscription.
        customer_id (int): The id of the customer.
        trainer_id (int): The id of the trainer.
        exercise_id (int): The id of the exercise plan.
    """

    id_counter: int = 1

    def __init__(self, date: str, customer_id: int, trainer_id: int, exercise_id: int) -> None:
        self.date = date
        self.customer_id = customer_id
        self.trainer_id = trainer_id
        self.exercise_id = exercise_id
        self.id = Subscription.id_counter
        Subscription.id_counter += 1

    @staticmethod
    def get_next_id() -> int:
        """
        Get the id that will be given to the next subscription.

        Returns:
            int: The next id number.
        """
        return Subscription.id_counter

    def __repr__(self) -> str:
        return f'Subscription <{self.id}> on {self.date}'
