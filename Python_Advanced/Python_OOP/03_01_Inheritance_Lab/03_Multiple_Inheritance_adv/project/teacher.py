from project.employee import Employee
from project.person import Person


class Teacher(Person, Employee):
    """
    This class is about a teacher that can teach, sleep and get fired.

    Methods:
        teach(): Says that the teacher is teaching.
    """

    # def teach(self) -> str:
    #     return 'teaching...'

    @staticmethod
    def teach() -> str:
        return 'teaching...'

    def __str__(self) -> str:
        return 'Teacher()'

    def __repr__(self) -> str:
        return 'Teacher()'

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Teacher)

    def __hash__(self) -> int:
        return hash('Teacher')


if __name__ == '__main__':
    # teacher_instance = Teacher()
    # print(teacher_instance.teach())
    pass
