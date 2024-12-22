def calculate_time(minutes_control, seconds_control, track_length, time_per_100m):
    control_time = minutes_control * 60 + seconds_control
    base_time = (track_length / 100) * time_per_100m
    reduction = (track_length / 120) * 2.5
    total_time = base_time - reduction

    return total_time, control_time


def main():
    mins_control = int(input())
    secs_control = int(input())
    track_len = float(input())
    secs_per_100m = int(input())

    total_time, control_time = calculate_time(mins_control, secs_control, track_len, secs_per_100m)

    if total_time <= control_time:
        print('Marin Bangiev won an Olympic quota!')
        print(f'His time is {total_time:.3f}.')
    else:
        diff = total_time - control_time
        print(f'No, Marin failed! He was {diff:.3f} second slower.')


if __name__ == '__main__':
    main()
