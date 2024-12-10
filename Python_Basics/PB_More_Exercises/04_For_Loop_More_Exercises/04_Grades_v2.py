n = int(input())
grades = []

for _ in range(n):
    grade = float(input())
    grades.append(grade)

top_students = 0
between_4_and_5 = 0
between_3_and_4 = 0
fail_students = 0
total_grade = 0

for grade in grades:
    total_grade += grade
    if grade >= 5.00:
        top_students += 1
    elif 4.00 <= grade < 5.00:
        between_4_and_5 += 1
    elif 3.00 <= grade < 4.00:
        between_3_and_4 += 1
    else:
        fail_students += 1

top_students_percent = (top_students / n) * 100
between_4_and_5_percent = (between_4_and_5 / n) * 100
between_3_and_4_percent = (between_3_and_4 / n) * 100
fail_students_percent = (fail_students / n) * 100

average_grade = total_grade / n

print(f'Top students: {top_students_percent:.2f}%')
print(f'Between 4.00 and 4.99: {between_4_and_5_percent:.2f}%')
print(f'Between 3.00 and 3.99: {between_3_and_4_percent:.2f}%')
print(f'Fail: {fail_students_percent:.2f}%')
print(f'Average: {average_grade:.2f}')
