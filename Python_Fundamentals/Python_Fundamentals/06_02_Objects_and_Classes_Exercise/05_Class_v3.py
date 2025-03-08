class Class:
    __students_count = 22

    def __init__(self, name: str):
        """Initializes the class with a name, and empty lists for students and grades."""
        self.name = name
        self.students = []
        self.grades = []

    def add_student(self, name: str, grade: float):
        """Adds a student and their grade if there is space available."""
        if len(self.students) < Class.__students_count:
            self.students.append(name)
            self.grades.append(grade)

    def get_average_grade(self) -> float:
        """Returns the average grade of all students formatted to 2 decimal places."""
        if not self.grades:
            return 0.0
        return round(sum(self.grades) / len(self.grades), 2)

    def __repr__(self) -> str:
        """Returns a formatted string representation of the class and students."""
        students_list = ', '.join(self.students)
        return f'The students in {self.name}: {students_list}. Average grade: {self.get_average_grade()}'
