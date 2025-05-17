class Employee:
    """
    This class is for an employee. It keeps the ID, name, and salary.

    Args:
        id (int): The ID of the employee
        first_name (str): The first name of the employee
        last_name (str): The last name of the employee
        salary (int): The monthly salary of the employee
    """

    def __init__(self, id: int, first_name: str, last_name: str, salary: int) -> None:
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def get_full_name(self) -> str:
        """
        This method returns the full name of the employee.

        Returns:
            str: The full name
        """
        return f'{self.first_name} {self.last_name}'

    def get_annual_salary(self) -> int:
        """
        This method returns the salary for the full year.

        Returns:
            int: Total yearly salary
        """
        return self.salary * 12

    def raise_salary(self, amount: int) -> int:
        """
        This method increases the salary by the given amount and returns it.

        Args:
            amount (int): The raise amount

        Returns:
            int: The new salary
        """
        self.salary += amount
        return self.salary

# if __name__ == '__main__':
#     emp_id = 1
#     emp_first = 'Jane'
#     emp_last = 'Doe'
#     emp_salary = 4000
#     emp_instance = Employee(id=emp_id, first_name=emp_first, last_name=emp_last, salary=emp_salary)
#     print(emp_instance.get_full_name())
#     print(emp_instance.get_annual_salary())
#     print(emp_instance.raise_salary(amount=500))
