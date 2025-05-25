from project.dark_wizard import DarkWizard


class SoulMaster(DarkWizard):
    """
    This class is about a soul master who is a kind of dark wizard.
    """

    # def __str__(self) -> str:
    #     return f'{self.username} of type {type(self).__name__} has level {self.level}'
    #
    # def __repr__(self) -> str:
    #     return f'SoulMaster(username={self.username}, level={self.level})'

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, SoulMaster):
            return False
        return self.username == other.username and self.level == other.level

    def __hash__(self) -> int:
        return hash((self.username, self.level))


if __name__ == '__main__':
    # soul_master_instance = SoulMaster(username='Zane', level=12)
    pass
