class Car:
    """
    Store car name, model, and engine.

    Args:
        name: brand of the car
        model: model of the car
        engine: engine description
    """

    def __init__(self, name: str, model: str, engine: str) -> None:
        self.name = name
        self.model = model
        self.engine = engine

    def get_info(self) -> str:
        """
        Return a string describing the car.

        Returns:
            Description of the car
        """
        return f'This is {self.name} {self.model} with engine {self.engine}'
