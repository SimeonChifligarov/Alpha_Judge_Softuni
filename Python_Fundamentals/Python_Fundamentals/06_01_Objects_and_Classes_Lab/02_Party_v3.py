class Party:
    """
    Represents a party with a list of attending people.
    """

    def __init__(self) -> None:
        self.people = []


if __name__ == '__main__':
    party_instance = Party()

    while True:
        name = input()
        if name == 'End':
            break
        party_instance.people.append(name)

    print(f'Going: {", ".join(party_instance.people)}')
    print(f'Total: {len(party_instance.people)}')
