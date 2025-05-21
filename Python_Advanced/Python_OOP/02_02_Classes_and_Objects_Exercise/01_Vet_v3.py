class Vet:
    """
    This class is for a veterinary doctor. It helps register and manage animals in a clinic.

    Args:
        name (str): The name of the vet doctor
    """

    animals = []
    space = 5

    def __init__(self, name: str) -> None:
        self.name = name
        self.animals = []

    def register_animal(self, animal_name: str) -> str:
        """
        This method registers an animal if there is space in the clinic.

        Args:
            animal_name (str): The name of the animal

        Returns:
            str: Message about the result
        """
        if len(Vet.animals) < Vet.space:
            Vet.animals.append(animal_name)
            self.animals.append(animal_name)
            return f'{animal_name} registered in the clinic'
        return 'Not enough space'

    def unregister_animal(self, animal_name: str) -> str:
        """
        This method removes an animal from the clinic.

        Args:
            animal_name (str): The name of the animal to remove

        Returns:
            str: Message about the result
        """
        if animal_name in Vet.animals:
            Vet.animals.remove(animal_name)
            if animal_name in self.animals:
                self.animals.remove(animal_name)
            return f'{animal_name} unregistered successfully'
        return f'{animal_name} not in the clinic'

    def info(self) -> str:
        """
        This method shows how many animals the vet has and how much space is left in the clinic.

        Returns:
            str: Vet info
        """
        return f'{self.name} has {len(self.animals)} animals. {Vet.space - len(Vet.animals)} space left in clinic'

    def __str__(self) -> str:
        return self.info()

    def __repr__(self) -> str:
        return f'Vet(name={self.name!r}, animals={self.animals!r})'

    # def __repr__(self) -> str:
    #     cls_name = self.__class__.__name__
    #     attrs = ', '.join(f'{k}={v!r}' for k, v in self.__dict__.items())
    #     return f'{cls_name}({attrs})'

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Vet):
            return self.name == other.name and self.animals == other.animals
        return NotImplemented

    def __gt__(self, other: object) -> bool:
        if isinstance(other, Vet):
            return len(self.animals) > len(other.animals)
        return NotImplemented

# if __name__ == '__main__':
#     vet_name_1 = 'Dr. Smith'
#     vet_name_2 = 'Dr. Jane'
#     vet_1 = Vet(name=vet_name_1)
#     vet_2 = Vet(name=vet_name_2)
#     print(vet_1.register_animal(animal_name='Buddy'))
#     print(vet_2.register_animal(animal_name='Milo'))
#     print(vet_1.register_animal(animal_name='Coco'))
#     print(vet_2.unregister_animal(animal_name='Max'))
#     print(vet_1.unregister_animal(animal_name='Buddy'))
#     print(vet_1.info())
#     print(vet_2.info())
#     print(str(vet_1))
#     print(repr(vet_2))
#     print(vet_1 == vet_2)
#     print(vet_1 > vet_2)
