def record_students_grades(number_of_students: int) -> None:
    """
    Read students' names and grades and print them with average grade.

    Args:
        number_of_students (int): Total number of students.

    Returns:
        None
    """
    students_record = {}
    for _ in range(number_of_students):
        student_info = input().split()
        student_name = student_info[0]
        student_grade = float(student_info[1])
        if student_name not in students_record:
            students_record[student_name] = []
        students_record[student_name].append(student_grade)
    for name, grades in students_record.items():
        grades_formatted = ' '.join(f'{grade:.2f}' for grade in grades)
        average_grade = sum(grades) / len(grades)
        print(f'{name} -> {grades_formatted} (avg: {average_grade:.2f})')


if __name__ == '__main__':
    students_count = int(input())
    record_students_grades(number_of_students=students_count)
