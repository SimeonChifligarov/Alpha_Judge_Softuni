# using while-else

max_poor_grades = int(input())
poor_grades_count = 0
total_grades = 0
problems_count = 0
last_problem = ''
command = input()

while command != 'Enough':
    problem_name = command
    grade = int(input())
    total_grades += grade
    problems_count += 1
    last_problem = problem_name

    if grade <= 4:
        poor_grades_count += 1
        if poor_grades_count >= max_poor_grades:
            print(f'You need a break, {poor_grades_count} poor grades.')
            break

    command = input()

else:
    average_score = total_grades / problems_count
    print(f'Average score: {average_score:.2f}')
    print(f'Number of problems: {problems_count}')
    print(f'Last problem: {last_problem}')
