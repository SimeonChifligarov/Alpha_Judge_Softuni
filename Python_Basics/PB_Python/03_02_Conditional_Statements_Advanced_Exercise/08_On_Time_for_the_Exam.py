exam_hour = int(input())
exam_minute = int(input())
arrival_hour = int(input())
arrival_minute = int(input())

exam_time_in_minutes = exam_hour * 60 + exam_minute
arrival_time_in_minutes = arrival_hour * 60 + arrival_minute

time_difference = arrival_time_in_minutes - exam_time_in_minutes

if time_difference > 0:
    print('Late')
    if time_difference < 60:
        print(f'{time_difference} minutes after the start')
    else:
        hours = time_difference // 60
        minutes = time_difference % 60
        print(f'{hours}:{minutes:02d} hours after the start')
elif time_difference < -30:
    print('Early')
    time_difference = abs(time_difference)
    if time_difference >= 60:
        hours = time_difference // 60
        minutes = time_difference % 60
        print(f'{hours}:{minutes:02d} hours before the start')
    else:
        print(f'{time_difference} minutes before the start')
else:
    print('On time')
    if time_difference:
        print(f'{-time_difference} minutes before the start')
