from project.formula_teams.formula_team import FormulaTeam


class RedBullTeam(FormulaTeam):
    """
    Class representing the Red Bull Formula 1 team.
    """

    def __init__(self, budget: int) -> None:
        super().__init__(budget=budget)

    def calculate_revenue_after_race(self, race_pos: int) -> str:
        revenue = 0

        if race_pos == 1:
            revenue += 1_500_000
        elif race_pos <= 2:
            revenue += 800_000

        if race_pos <= 8:
            revenue += 20_000
        elif race_pos <= 10:
            revenue += 10_000

        revenue -= 250_000
        self.budget += revenue

        return f'The revenue after the race is {revenue}$. Current budget {self.budget}$'
