from collections import defaultdict


def read_student_grades() -> dict[str, list[float]]:
    """
    Reads student names and grades from input.
    Returns a dictionary where keys are student names and values are lists of grades.
    """
    n = int(input())
    students = defaultdict(list)

    for _ in range(n):
        name = input()
        grade = float(input())
        students[name].append(grade)

    return students


def filter_and_print_students(students: dict[str, list[float]]) -> None:
    """
    Filters students with an average grade of 4.50 or higher and prints their names with the formatted average grade.
    """
    for name, grades in students.items():
        average_grade = sum(grades) / len(grades)
        if average_grade >= 4.50:
            print(f'{name} -> {average_grade:.2f}')


if __name__ == '__main__':
    student_data = read_student_grades()
    filter_and_print_students(students=student_data)
