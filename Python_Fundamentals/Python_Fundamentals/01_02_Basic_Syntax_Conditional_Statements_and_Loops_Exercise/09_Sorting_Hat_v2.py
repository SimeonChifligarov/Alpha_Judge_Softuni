def sort_students(student_names):
    results = []
    for student in student_names:
        if student == 'Voldemort':
            results.append('You must not speak of that name!')
            return results

        if len(student) < 5:
            results.append(f'{student} goes to Gryffindor.')
        elif len(student) == 5:
            results.append(f'{student} goes to Slytherin.')
        elif len(student) == 6:
            results.append(f'{student} goes to Ravenclaw.')
        else:
            results.append(f'{student} goes to Hufflepuff.')
    results.append('Welcome to Hogwarts.')
    return results


if __name__ == '__main__':
    names = []
    while True:
        current_name = input()
        if current_name == 'Welcome!':
            break
        names.append(current_name)
        if current_name == 'Voldemort':
            break

    sorting_results = sort_students(student_names=names)

    for result in sorting_results:
        print(result)
