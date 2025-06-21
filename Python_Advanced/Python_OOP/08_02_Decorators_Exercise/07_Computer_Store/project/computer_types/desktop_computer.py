from project.computer_types.computer import Computer


class DesktopComputer(Computer):
    """
    Desktop computer that can be configured.
    """

    available_processors = {
        'AMD Ryzen 7 5700G': 500,
        'Intel Core i5-12600K': 600,
        'Apple M1 Max': 1800,
    }

    max_ram = 128

    def __init__(self, manufacturer: str, model: str) -> None:
        super().__init__(manufacturer=manufacturer, model=model)

    def configure_computer(self, processor: str, ram: int) -> str:
        if processor not in self.available_processors:
            raise ValueError(f'{processor} is not compatible with desktop computer {self.manufacturer} {self.model}!')
        if ram > self.max_ram or (ram & (ram - 1)) != 0:
            raise ValueError(f'{ram}GB RAM is not compatible with desktop computer {self.manufacturer} {self.model}!')
        self.processor = processor
        self.ram = ram
        self.price = self.available_processors[processor] + (ram.bit_length() - 1) * 100
        return f'Created {self.manufacturer} {self.model} with {self.processor} and {self.ram}GB RAM for {self.price}$.'
