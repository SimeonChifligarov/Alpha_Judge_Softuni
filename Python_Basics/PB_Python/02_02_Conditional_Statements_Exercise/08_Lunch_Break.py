import math

serial_name = input()
episode_duration = int(input())
break_duration = int(input())

lunch_time = break_duration / 8
rest_time = break_duration / 4
available_time = break_duration - lunch_time - rest_time

if available_time >= episode_duration:
    remaining_time = available_time - episode_duration
    print(f'You have enough time to watch {serial_name} and left with {math.ceil(remaining_time)} minutes free time.')
else:
    needed_time = episode_duration - available_time
    print(f"You don't have enough time to watch {serial_name}, you need {math.ceil(needed_time)} more minutes.")
