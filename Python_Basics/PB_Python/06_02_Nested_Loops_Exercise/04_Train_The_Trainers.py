judges_count = int(input())
presentation_count = 0
total_sum = 0

presentation_name = input()

while presentation_name != 'Finish':
    grades = [float(input()) for _ in range(judges_count)]
    average_grade = sum(grades) / len(grades)

    print(f'{presentation_name} - {average_grade:.2f}.')

    total_sum += average_grade
    presentation_count += 1

    presentation_name = input()

final_average = total_sum / presentation_count
print(f'Student\'s final assessment is {final_average:.2f}.')
