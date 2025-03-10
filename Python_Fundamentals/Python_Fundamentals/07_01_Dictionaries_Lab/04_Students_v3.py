def read_input() -> tuple[list[str], str]:
    """Reads student data and course name from input."""
    students = []

    while True:
        data = input()
        if ':' not in data:
            return students, data
        students.append(data)


def filter_students_by_course(student_data: list[str], target_course: str) -> list[str]:
    """Filters students based on the given course and returns formatted output."""
    return [
        f'{name} - {student_id}'
        for entry in student_data
        for name, student_id, course in [entry.split(':')]
        if course.replace(' ', '_') == target_course
    ]


if __name__ == '__main__':
    student_records, course_name = read_input()
    results = filter_students_by_course(student_data=student_records, target_course=course_name)
    print('\n'.join(results))
