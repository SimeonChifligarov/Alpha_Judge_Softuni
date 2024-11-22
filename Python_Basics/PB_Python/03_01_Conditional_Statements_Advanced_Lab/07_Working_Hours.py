valid_days = [
    'Monday',
    'Tuesday',
    'Wednesday',
    'Thursday',
    'Friday',
    'Saturday',
]

hour = int(input())
day = input()

is_valid_hour = 10 <= hour < 18
is_open = is_valid_hour and day in valid_days

print('open' if is_open else 'closed')
