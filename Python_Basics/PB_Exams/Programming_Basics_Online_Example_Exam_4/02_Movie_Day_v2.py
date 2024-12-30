def check_film_schedule(shooting_time, scene_count, scene_duration):
    preparation_time = shooting_time * 0.15
    filming_time = scene_count * scene_duration
    total_time_needed = preparation_time + filming_time

    if total_time_needed <= shooting_time:
        remaining_time = round(shooting_time - total_time_needed)
        return f'You managed to finish the movie on time! You have {remaining_time} minutes left!'
    else:
        extra_time = round(total_time_needed - shooting_time)
        return f'Time is up! To complete the movie you need {extra_time} minutes.'


shoot_time = int(input())
scenes = int(input())
scene_time = int(input())

result = check_film_schedule(shoot_time, scenes, scene_time)
print(result)
