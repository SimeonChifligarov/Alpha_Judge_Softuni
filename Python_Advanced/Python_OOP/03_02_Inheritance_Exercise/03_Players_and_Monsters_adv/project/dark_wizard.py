from project.wizard import Wizard


class DarkWizard(Wizard):
    """
    This class is about a dark wizard who is a kind of wizard.
    """

    # def __str__(self) -> str:
    #     return 'DarkWizard()'
    #
    # def __repr__(self) -> str:
    #     return 'DarkWizard()'

    def __eq__(self, other: object) -> bool:
        return isinstance(other, DarkWizard)

    def __hash__(self) -> int:
        return hash('DarkWizard')


if __name__ == '__main__':
    # dark_wizard_instance = DarkWizard()
    pass
