def collect_students_data() -> tuple[dict[str, list[tuple[str, str]]], str]:
    """Collects student data from user input and organizes it by course."""
    students: dict[str, list[tuple[str, str]]] = {}

    while True:
        entry = input()
        if ':' not in entry:
            target_course = entry.replace('_', ' ')
            return students, target_course

        name, student_id, course = entry.split(':')
        if course not in students:
            students[course] = []
        students[course].append((name, student_id))


def print_students_in_course(students: dict, course_name: str) -> None:
    """Prints students enrolled in a given course."""
    if course_name in students:
        for name, student_id in students[course_name]:
            print(f'{name} - {student_id}')
    else:
        print('No students found for this course.')


if __name__ == '__main__':
    students_data, selected_course = collect_students_data()
    print_students_in_course(students=students_data, course_name=selected_course)
