class Employee:
    """
    This class is about an employee that can get fired.

    Methods:
        get_fired(): Says that the employee is fired.
    """

    # def get_fired(self) -> str:
    #     return 'fired...'

    @staticmethod
    def get_fired() -> str:
        return 'fired...'

    def __str__(self) -> str:
        return 'Employee()'

    def __repr__(self) -> str:
        return 'Employee()'

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Employee)

    def __hash__(self) -> int:
        return hash('Employee')


if __name__ == '__main__':
    # employee_instance = Employee()
    # print(employee_instance.get_fired())
    pass
