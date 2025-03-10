def filter_students_by_course(student_data: list[str], target_course: str) -> list[str]:
    """Filters students based on the given course and returns formatted output."""
    return [
        f'{name} - {student_id}'
        for entry in student_data
        for name, student_id, course in [entry.split(':')]
        if course.replace(' ', '_') == target_course
    ]


if __name__ == '__main__':
    students = []

    while True:
        data = input()
        if ':' not in data:
            course_name = data
            break
        students.append(data)

    results = filter_students_by_course(student_data=students, target_course=course_name)
    print('\n'.join(results))
