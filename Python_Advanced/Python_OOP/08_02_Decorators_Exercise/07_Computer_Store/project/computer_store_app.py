from project.computer_types.desktop_computer import DesktopComputer
from project.computer_types.laptop import Laptop


class ComputerStoreApp:
    """
    This class handles building and selling computers.
    """

    def __init__(self) -> None:
        self.warehouse = []
        self.profits = 0

    def build_computer(self, type_computer: str, manufacturer: str, model: str, processor: str, ram: int) -> str:
        if type_computer not in ('Desktop Computer', 'Laptop'):
            raise ValueError(f'{type_computer} is not a valid type computer!')
        if type_computer == 'Desktop Computer':
            computer = DesktopComputer(manufacturer=manufacturer, model=model)
        else:
            computer = Laptop(manufacturer=manufacturer, model=model)
        configuration_message = computer.configure_computer(processor=processor, ram=ram)
        self.warehouse.append(computer)
        return configuration_message

    def sell_computer(self, client_budget: int, wanted_processor: str, wanted_ram: int) -> str:
        for computer in self.warehouse:
            if (computer.processor == wanted_processor
                    and computer.ram >= wanted_ram
                    and computer.price <= client_budget):
                self.warehouse.remove(computer)
                self.profits += client_budget - computer.price
                return f'{computer} sold for {client_budget}$.'
        raise Exception("Sorry, we don't have a computer for you.")
