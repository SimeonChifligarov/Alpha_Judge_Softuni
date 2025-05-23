from project.employee import Employee
from project.person import Person


class Teacher(Person, Employee):
    """
    This class is about a teacher that can teach, sleep and get fired.

    Methods:
        teach(): Says that the teacher is teaching.
    """

    def teach(self) -> str:
        return 'teaching...'


if __name__ == '__main__':
    # teacher_instance = Teacher()
    # print(teacher_instance.teach())
    pass
