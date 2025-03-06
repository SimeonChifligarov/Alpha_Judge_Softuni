class Zoo:
    """
    Represents a zoo with categorized animals stored in a dictionary and a total count tracker.
    """

    __animals = 0

    def __init__(self, zoo_name: str) -> None:
        self.zoo_name = zoo_name
        self.animals = {'mammal': [], 'fish': [], 'bird': []}

    def add_animal(self, species: str, name: str) -> None:
        if species in self.animals:
            self.animals[species].append(name)
            Zoo.__animals += 1

    def get_info(self, species: str) -> str:
        if species in self.animals:
            names = ', '.join(self.animals[species])
            return f'{species.capitalize() if species != "fish" else species.capitalize() + "e"}s in {self.zoo_name}: {names}\nTotal animals: {Zoo.__animals}'
        return 'Invalid species'


if __name__ == '__main__':
    zoo_instance = Zoo(zoo_name=input())
    for _ in range(int(input())):
        species_type, animal_name = input().split()
        zoo_instance.add_animal(species=species_type, name=animal_name)

    requested_species = input()
    print(zoo_instance.get_info(species=requested_species))
