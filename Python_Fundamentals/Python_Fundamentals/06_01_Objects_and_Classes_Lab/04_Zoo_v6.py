class Zoo:
    """
    Represents a zoo with categorized animals stored in a dictionary and a total count tracker.
    """

    __animals = 0

    def __init__(self, zoo_name: str) -> None:
        self.zoo_name = zoo_name
        self._animals = {'mammal': [], 'fish': [], 'bird': []}

    @property
    def mammals(self) -> list[str]:
        return self._animals['mammal']

    @property
    def fishes(self) -> list[str]:
        return self._animals['fish']

    @property
    def birds(self) -> list[str]:
        return self._animals['bird']

    @staticmethod
    def format_species(species: str) -> str:
        special_species = {
            'fish': 'Fishes',
        }
        return special_species.get(species, species.capitalize() + 's')

    def add_animal(self, species: str, name: str) -> None:
        if species in self._animals:
            self._animals[species].append(name)
            Zoo.__animals += 1

    def get_info(self, species: str) -> str:
        if species in self._animals:
            names = ', '.join(self._animals[species])
            return f'{self.format_species(species)} in {self.zoo_name}: {names}\nTotal animals: {Zoo.__animals}'
        return 'Invalid species'


if __name__ == '__main__':
    zoo_instance = Zoo(zoo_name=input())

    for _ in range(int(input())):
        species_type, animal_name = input().split()
        zoo_instance.add_animal(species=species_type, name=animal_name)

    requested_species = input()
    print(zoo_instance.get_info(species=requested_species))
