from project.formula_teams.red_bull_team import RedBullTeam
from project.formula_teams.mercedes_team import MercedesTeam


class F1SeasonApp:
    """
    Class representing the F1 Season App.

    Manages the registration and race results for teams.
    """

    def __init__(self) -> None:
        self.red_bull_team = None
        self.mercedes_team = None

    def register_team_for_season(self, team_name: str, budget: int) -> str:
        if team_name == 'Red Bull':
            self.red_bull_team = RedBullTeam(budget=budget)
            return f'{team_name} has joined the new F1 season.'
        elif team_name == 'Mercedes':
            self.mercedes_team = MercedesTeam(budget=budget)
            return f'{team_name} has joined the new F1 season.'
        else:
            raise ValueError('Invalid team name!')

    def new_race_results(self, race_name: str, red_bull_pos: int, mercedes_pos: int) -> str:
        if self.red_bull_team is None or self.mercedes_team is None:
            raise Exception('Not all teams have registered for the season.')

        red_bull_revenue_msg = self.red_bull_team.calculate_revenue_after_race(race_pos=red_bull_pos)
        mercedes_revenue_msg = self.mercedes_team.calculate_revenue_after_race(race_pos=mercedes_pos)

        if red_bull_pos < mercedes_pos:
            leading_team = 'Red Bull'
        else:
            leading_team = 'Mercedes'

        return (
            f'Red Bull: {red_bull_revenue_msg}. '
            f'Mercedes: {mercedes_revenue_msg}. '
            f'{leading_team} is ahead at the {race_name} race.'
        )
