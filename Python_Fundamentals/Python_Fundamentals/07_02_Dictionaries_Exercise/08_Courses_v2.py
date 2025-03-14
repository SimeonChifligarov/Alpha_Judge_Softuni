def register_students() -> dict[str, list[str]]:
    """
    Reads course registration data and stores it in a dictionary.
    Returns a dictionary where keys are course names and values are lists of registered students.
    """
    courses = {}

    while True:
        data = input()
        if data == 'end':
            break

        course_name, student_name = data.split(' : ', maxsplit=1)

        if course_name not in courses:
            courses[course_name] = []

        courses[course_name].append(student_name)

    return courses


def print_courses(courses: dict[str, list[str]]) -> None:
    """
    Prints course names with the total number of registered students.
    Also prints the list of students for each course.
    """
    for course, students in courses.items():
        print(f'{course}: {len(students)}')
        for student in students:
            print(f'-- {student}')


if __name__ == '__main__':
    course_data = register_students()
    print_courses(courses=course_data)
