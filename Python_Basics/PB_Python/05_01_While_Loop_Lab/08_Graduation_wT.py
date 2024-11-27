# using while True

name = input()
grade = 1
failed_count = 0
total_grades = 0

while True:
    current_grade = float(input())

    if current_grade < 4.00:
        failed_count += 1
        if failed_count > 1:
            print(f'{name} has been excluded at {grade} grade')
            break
    else:
        grade += 1
        total_grades += current_grade

    if grade > 12:
        average_grade = total_grades / 12
        print(f'{name} graduated. Average grade: {average_grade:.2f}')
        break
