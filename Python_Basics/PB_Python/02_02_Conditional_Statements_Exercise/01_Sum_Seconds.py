first_athlete_time = int(input())
second_athlete_time = int(input())
third_athlete_time = int(input())

total_time_in_seconds = first_athlete_time + second_athlete_time + third_athlete_time

minutes = total_time_in_seconds // 60
seconds = total_time_in_seconds % 60

print(f'{minutes}:{seconds:02d}')
