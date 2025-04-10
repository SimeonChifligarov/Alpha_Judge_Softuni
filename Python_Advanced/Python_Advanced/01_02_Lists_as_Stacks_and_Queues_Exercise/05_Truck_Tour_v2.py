def find_starting_pump(petrol_pumps: list[tuple[int, int]]) -> int:
    """
    Finds the first petrol pump index to complete the circle.

    Args:
        petrol_pumps: A list of tuples where each tuple has petrol amount and distance to next pump.

    Returns:
        The index of the first suitable petrol pump.
    """
    total_petrol = 0
    total_distance = 0
    current_petrol = 0
    start_index = 0
    for idx in range(len(petrol_pumps)):
        petrol, distance = petrol_pumps[idx]
        total_petrol += petrol
        total_distance += distance
        current_petrol += petrol - distance
        if current_petrol < 0:
            start_index = idx + 1
            current_petrol = 0
    if total_petrol >= total_distance:
        return start_index
    return -1


if __name__ == '__main__':
    number_of_pumps = int(input())
    pumps_data = [(int(values[0]), int(values[1])) for values in (input().split() for _ in range(number_of_pumps))]
    starting_index = find_starting_pump(petrol_pumps=pumps_data)
    print(starting_index)
