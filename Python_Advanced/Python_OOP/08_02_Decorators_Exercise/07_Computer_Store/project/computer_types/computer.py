from abc import ABC, abstractmethod


class Computer(ABC):
    """
    Abstract base class for computers.
    """

    def __init__(self, manufacturer: str, model: str) -> None:
        self.manufacturer = manufacturer
        self.model = model
        self.processor = None
        self.ram = None
        self.price = 0

    @property
    def manufacturer(self) -> str:
        return self.__manufacturer

    @manufacturer.setter
    def manufacturer(self, value: str) -> None:
        if not value.strip():
            raise ValueError('Manufacturer name cannot be empty.')
        self.__manufacturer = value

    @property
    def model(self) -> str:
        return self.__model

    @model.setter
    def model(self, value: str) -> None:
        if not value.strip():
            raise ValueError('Model name cannot be empty.')
        self.__model = value

    @abstractmethod
    def configure_computer(self, processor: str, ram: int) -> str:
        """
        Configure the computer with processor and RAM.
        """
        pass

    def __repr__(self) -> str:
        return f'{self.manufacturer} {self.model} with {self.processor} and {self.ram}GB RAM'
