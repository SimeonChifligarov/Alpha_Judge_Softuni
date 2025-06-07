from abc import ABC, abstractmethod


class FormulaTeam(ABC):
    """
    Abstract class representing a Formula 1 team.

    Args:
        budget (int): The team's initial budget.
    """

    def __init__(self, budget: int) -> None:
        self.budget = budget

    @property
    def budget(self) -> int:
        return self.__budget

    @budget.setter
    def budget(self, value: int) -> None:
        if value < 1_000_000:
            raise ValueError('F1 is an expensive sport, find more sponsors!')
        self.__budget = value

    @abstractmethod
    def calculate_revenue_after_race(self, race_pos: int) -> str:
        pass

