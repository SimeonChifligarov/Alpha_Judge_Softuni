from project.player import Player


class Team:
    """
    This class is about a football team with players and a rating.

    Args:
        name (str): The name of the team.
        rating (int): The rating of the team.
    """

    def __init__(self, name: str, rating: int) -> None:
        self.__name = name
        self.__rating = rating
        self.__players: list[Player] = []

    def add_player(self, player: Player) -> str:
        if player in self.__players:
            return f'Player {player.name} has already joined'
        self.__players.append(player)
        return f'Player {player.name} joined team {self.__name}'

    def remove_player(self, player_name: str) -> str | Player:
        player_to_remove = next((p for p in self.__players if p.name == player_name), None)
        if player_to_remove is None:
            return f'Player {player_name} not found'
        self.__players.remove(player_to_remove)
        return player_to_remove


if __name__ == '__main__':
    pass
