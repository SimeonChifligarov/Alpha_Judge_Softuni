from project.elf import Elf


class MuseElf(Elf):
    """
    This class is about a muse elf who is a kind of elf.
    """

    # def __str__(self) -> str:
    #     return f'{self.username} of type {type(self).__name__} has level {self.level}'
    #
    # def __repr__(self) -> str:
    #     return f'MuseElf(username={self.username}, level={self.level})'

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, MuseElf):
            return False
        return self.username == other.username and self.level == other.level

    def __hash__(self) -> int:
        return hash((self.username, self.level))


if __name__ == '__main__':
    # muse_elf_instance = MuseElf(username='Lira', level=8)
    pass
