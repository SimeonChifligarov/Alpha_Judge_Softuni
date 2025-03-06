class Zoo:
    """
    Represents a zoo with categorized animals and a total count tracker.
    """

    __animals = 0

    def __init__(self, zoo_name: str) -> None:
        self.zoo_name = zoo_name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species: str, name: str) -> None:
        if species == 'mammal':
            self.mammals.append(name)
        elif species == 'fish':
            self.fishes.append(name)
        elif species == 'bird':
            self.birds.append(name)
        Zoo.__animals += 1

    def get_info(self, species: str) -> str:
        if species == 'mammal':
            names = ', '.join(self.mammals)
        elif species == 'fish':
            names = ', '.join(self.fishes)
            species += 'e'
        elif species == 'bird':
            names = ', '.join(self.birds)
        else:
            return 'Invalid species'

        return f'{species.capitalize()}s in {self.zoo_name}: {names}\nTotal animals: {Zoo.__animals}'


if __name__ == '__main__':
    zoo_instance = Zoo(zoo_name=input())
    for _ in range(int(input())):
        species_type, animal_name = input().split()
        zoo_instance.add_animal(species=species_type, name=animal_name)

    requested_species = input()
    print(zoo_instance.get_info(species=requested_species))
