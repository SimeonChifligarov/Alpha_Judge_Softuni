from project.hero import Hero


class Elf(Hero):
    """
    This class is about an elf who is a kind of hero.
    """

    # def __str__(self) -> str:
    #     return 'Elf()'
    #
    # def __repr__(self) -> str:
    #     return 'Elf()'

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Elf)

    def __hash__(self) -> int:
        return hash('Elf')


if __name__ == '__main__':
    # elf_instance = Elf()
    pass
