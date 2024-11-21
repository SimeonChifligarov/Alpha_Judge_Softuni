age = float(input())
gender = input()

result = ''

if gender == 'm':
    if age >= 16:
        result = 'Mr.'
    else:
        result = 'Master'
elif gender == 'f':
    if age >= 16:
        result = 'Ms.'
    else:
        result = 'Miss'

if not result:
    print('Invalid input')
    exit(5)

print(result)
