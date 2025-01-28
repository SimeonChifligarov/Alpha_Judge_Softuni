def convert_centuries_to_time(centuries):
    total_years = centuries * 100
    total_days = int(total_years * 365.2422)
    total_hours = total_days * 24
    total_minutes = total_hours * 60
    return total_years, total_days, total_hours, total_minutes


if __name__ == '__main__':
    centuries_input = int(input())
    years, days, hours, minutes = convert_centuries_to_time(centuries=centuries_input)
    print(f'{centuries_input} centuries = {years} years = {days} days = {hours} hours = {minutes} minutes')
