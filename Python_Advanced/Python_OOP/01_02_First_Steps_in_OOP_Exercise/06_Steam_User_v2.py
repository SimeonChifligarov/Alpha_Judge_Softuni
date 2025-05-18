class SteamUser:
    """
    This class is for a Steam user. It holds the username, games, and total play time.

    Args:
        username (str): The username of the player
        games (list): The list of games in their library
    """

    def __init__(self, username: str, games: list) -> None:
        self.username = username
        self.games = games
        self.played_hours = 0

    def play(self, game: str, hours: int) -> str:
        """
        This method lets the user play a game. If it's in the library, it adds play time.

        Args:
            game (str): The game to play
            hours (int): Hours to play

        Returns:
            str: Info about playing or missing game
        """
        if game in self.games:
            self.played_hours += hours
            return f'{self.username} is playing {game}'
        return f'{game} is not in library'

    def buy_game(self, game: str) -> str:
        """
        This method adds a new game if it's not already owned.

        Args:
            game (str): The game to buy

        Returns:
            str: Info about buying or already owned
        """
        if game not in self.games:
            self.games.append(game)
            return f'{self.username} bought {game}'
        return f'{game} is already in your library'

    def status(self) -> str:
        """
        This method shows how many games the user has and total play time.

        Returns:
            str: Status report
        """
        return f'{self.username} has {len(self.games)} games. Total play time: {self.played_hours}'

# if __name__ == '__main__':
#     user_name = 'player123'
#     game_list = ['CS2', 'Dota 2']
#     steam_instance = SteamUser(username=user_name, games=game_list)
#     print(steam_instance.play(game='CS2', hours=3))
#     print(steam_instance.play(game='Valorant', hours=2))
#     print(steam_instance.buy_game(game='Valorant'))
#     print(steam_instance.buy_game(game='Dota 2'))
#     print(steam_instance.status())
