def find_race_winner(race_times: list[int]) -> str:
    """
    Determines the winner of the race based on the sequence of times for each car.
    The left car starts from the left and the right car starts from the right, meeting at the middle.
    Zeroes in the sequence reduce the racer's time by 20%.
    """

    mid_index = len(race_times) // 2
    left_car_times = race_times[:mid_index]
    right_car_times = race_times[mid_index + 1:][::-1]

    left_total_time = 0
    for time in left_car_times:
        if time == 0:
            left_total_time *= 0.8
        else:
            left_total_time += time

    right_total_time = 0
    for time in right_car_times:
        if time == 0:
            right_total_time *= 0.8
        else:
            right_total_time += time

    if left_total_time < right_total_time:
        return f'The winner is left with total time: {left_total_time:.1f}'
    else:
        return f'The winner is right with total time: {right_total_time:.1f}'


if __name__ == '__main__':
    race_data = list(map(int, input().split()))
    result = find_race_winner(race_times=race_data)
    print(result)
