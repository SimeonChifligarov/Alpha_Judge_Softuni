class Zoo:
    """
    This class is about a zoo that manages animals and workers.

    Args:
        name (str): The name of the zoo.
        budget (int): The budget of the zoo.
        animal_capacity (int): The max number of animals.
        workers_capacity (int): The max number of workers.
    """

    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int) -> None:
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal: object, price: int) -> str:
        if self.__animal_capacity <= len(self.animals):
            return 'Not enough space for animal'
        if self.__budget < price:
            return 'Not enough budget'
        self.animals.append(animal)
        self.__budget -= price
        return f'{animal.name} the {animal.__class__.__name__} added to the zoo'

    def hire_worker(self, worker: object) -> str:
        if self.__workers_capacity <= len(self.workers):
            return 'Not enough space for worker'
        self.workers.append(worker)
        return f'{worker.name} the {worker.__class__.__name__} hired successfully'

    def fire_worker(self, worker_name: str) -> str:
        worker_to_fire = next((w for w in self.workers if w.name == worker_name), None)
        if worker_to_fire is None:
            return f'There is no {worker_name} in the zoo'
        self.workers.remove(worker_to_fire)
        return f'{worker_name} fired successfully'

    def pay_workers(self) -> str:
        total_salaries = sum(worker.salary for worker in self.workers)
        if self.__budget >= total_salaries:
            self.__budget -= total_salaries
            return f'You payed your workers. They are happy. Budget left: {self.__budget}'
        return 'You have no budget to pay your workers. They are unhappy'

    def tend_animals(self) -> str:
        total_care = sum(animal.money_for_care for animal in self.animals)
        if self.__budget >= total_care:
            self.__budget -= total_care
            return f'You tended all the animals. They are happy. Budget left: {self.__budget}'
        return 'You have no budget to tend the animals. They are unhappy.'

    def profit(self, amount: int) -> None:
        self.__budget += amount

    def animals_status(self) -> str:
        lions = [a for a in self.animals if a.__class__.__name__ == 'Lion']
        tigers = [a for a in self.animals if a.__class__.__name__ == 'Tiger']
        cheetahs = [a for a in self.animals if a.__class__.__name__ == 'Cheetah']
        result = [f'You have {len(self.animals)} animals']
        result.append(f'----- {len(lions)} Lions:')
        result.extend(str(lion) for lion in lions)
        result.append(f'----- {len(tigers)} Tigers:')
        result.extend(str(tiger) for tiger in tigers)
        result.append(f'----- {len(cheetahs)} Cheetahs:')
        result.extend(str(cheetah) for cheetah in cheetahs)
        return '\n'.join(result)

    def workers_status(self) -> str:
        keepers = [w for w in self.workers if w.__class__.__name__ == 'Keeper']
        caretakers = [w for w in self.workers if w.__class__.__name__ == 'Caretaker']
        vets = [w for w in self.workers if w.__class__.__name__ == 'Vet']
        result = [f'You have {len(self.workers)} workers']
        result.append(f'----- {len(keepers)} Keepers:')
        result.extend(str(keeper) for keeper in keepers)
        result.append(f'----- {len(caretakers)} Caretakers:')
        result.extend(str(caretaker) for caretaker in caretakers)
        result.append(f'----- {len(vets)} Vets:')
        result.extend(str(vet) for vet in vets)
        return '\n'.join(result)


if __name__ == '__main__':
    pass
