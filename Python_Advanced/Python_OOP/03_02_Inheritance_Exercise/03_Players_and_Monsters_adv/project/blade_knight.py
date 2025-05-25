from project.dark_knight import DarkKnight


class BladeKnight(DarkKnight):
    """
    This class is about a blade knight who is a kind of dark knight.
    """

    # def __str__(self) -> str:
    #     return 'BladeKnight()'
    #
    # def __repr__(self) -> str:
    #     return 'BladeKnight()'

    def __eq__(self, other: object) -> bool:
        return isinstance(other, BladeKnight)

    def __hash__(self) -> int:
        return hash('BladeKnight')


if __name__ == '__main__':
    # blade_knight_instance = BladeKnight()
    pass
