from project.knight import Knight


class DarkKnight(Knight):
    """
    This class is about a dark knight who is a kind of knight.
    """

    # def __str__(self) -> str:
    #     return 'DarkKnight()'
    #
    # def __repr__(self) -> str:
    #     return 'DarkKnight()'

    def __eq__(self, other: object) -> bool:
        return isinstance(other, DarkKnight)

    def __hash__(self) -> int:
        return hash('DarkKnight')


if __name__ == '__main__':
    # dark_knight_instance = DarkKnight()
    pass
