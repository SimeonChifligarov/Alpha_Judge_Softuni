age = float(input())
gender = input()

titles = {
    'm': {
        True: 'Mr.',
        False: 'Master',
    },
    'f': {
        True: 'Ms.',
        False: 'Miss',
    },
}

is_adult = age >= 16

print(titles.get(gender, {}).get(is_adult, 'Invalid input'))
