from project.hero import Hero


class Wizard(Hero):
    """
    This class is about a wizard who is a kind of hero.
    """

    # def __str__(self) -> str:
    #     return f'{self.username} of type {type(self).__name__} has level {self.level}'
    #
    # def __repr__(self) -> str:
    #     return f'Wizard(username={self.username}, level={self.level})'

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Wizard):
            return False
        return self.username == other.username and self.level == other.level

    def __hash__(self) -> int:
        return hash((self.username, self.level))


if __name__ == '__main__':
    # wizard_instance = Wizard(username='Merlin', level=30)
    pass
