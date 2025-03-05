class Party:
    def __init__(self) -> None:
        self.people = []

    def add_person(self, name: str) -> None:
        """Adds a person to the party list."""

        self.people.append(name)

    def display_summary(self) -> None:
        """Displays the list of people and total count."""

        print(f'Going: {", ".join(self.people)}')
        print(f'Total: {len(self.people)}')


if __name__ == '__main__':
    party = Party()

    while True:
        name_input = input()
        if name_input == 'End':
            break

        party.add_person(name_input)

    party.display_summary()
