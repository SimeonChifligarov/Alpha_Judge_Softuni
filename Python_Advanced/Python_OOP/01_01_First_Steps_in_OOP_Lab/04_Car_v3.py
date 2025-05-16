class Car:
    """
    Store and describe a car.

    Args:
        name: car brand
        model: car model
        engine: car engine
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

    def __str__(self) -> str:
        return self.get_info()

    def __repr__(self) -> str:
        return f'Car(name={self.name!r}, model={self.model!r}, engine={self.engine!r})'

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Car):
            return False
        return self.name == other.name and self.model == other.model and self.engine == other.engine

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, Car):
            return NotImplemented
        return (self.name, self.model, self.engine) < (other.name, other.model, other.engine)
