# 1 centuries = 100 years = 36524 days = 876576 hours = 52594560 minutes

DAYS_IN_YEAR = 365.2422

centuries = int(input())

years = centuries * 100
days = int(years * DAYS_IN_YEAR)
hours = days * 24
minutes = hours * 60

print(f'{centuries} centuries = {years} years = {days} days = {hours} hours = {minutes} minutes')
