def convert_centuries_to_time(cent):
    days_in_year = 365.2422
    total_years = cent * 100
    total_days = int(total_years * days_in_year)
    total_hours = total_days * 24
    total_minutes = total_hours * 60
    return total_years, total_days, total_hours, total_minutes


if __name__ == '__main__':
    centuries_value = int(input())
    result_years, result_days, result_hours, result_minutes = convert_centuries_to_time(cent=centuries_value)
    print(
        f'{centuries_value} centuries = {result_years} years = {result_days} days = {result_hours} '
        f'hours = {result_minutes} minutes'
    )
