class Class:
    """
    Represents a class with students, grades, and a maximum student count.
    """

    __students_count = 22

    def __init__(self, name: str) -> None:
        self.name = name
        self.students = []
        self.grades = []

    def add_student(self, name: str, grade: float) -> None:
        if len(self.students) < self.__students_count:
            self.students.append(name)
            self.grades.append(grade)

    def get_average_grade(self) -> float:
        return round(sum(self.grades) / len(self.grades), 2) if self.grades else 0.0

    def __repr__(self) -> str:
        students_list = ', '.join(self.students)
        return f'The students in {self.name}: {students_list}. Average grade: {self.get_average_grade()}'

# if __name__ == '__main__':
#     class_instance = Class(name=input())
#
#     for _ in range(int(input())):
#         student_name, student_grade = input().split()
#         class_instance.add_student(name=student_name, grade=float(student_grade))
#
#     print(class_instance)
