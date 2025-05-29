class Worker:
    """
    This class is about a worker at the zoo.

    Args:
        name (str): The name of the worker.
        age (int): The age of the worker.
        salary (int): The salary of the worker.
    """

    def __init__(self, name: str, age: int, salary: int) -> None:
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self) -> str:
        return f'Name: {self.name}, Age: {self.age}, Salary: {self.salary}'


if __name__ == '__main__':
    pass
