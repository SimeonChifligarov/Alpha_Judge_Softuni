def get_starting_pump(pumps: list[tuple[int, int]]) -> int:
    """
    Works out the first petrol pump index you can start from to finish the circle.

    Args:
        pumps: A list where each item has two numbers: petrol given and distance to next pump.

    Returns:
        The index of the first good petrol pump.
    """
    total_balance = 0
    current_balance = 0
    start_pump = 0
    for pump_index, (fuel, distance_needed) in enumerate(pumps):
        balance = fuel - distance_needed
        total_balance += balance
        current_balance += balance
        if current_balance < 0:
            start_pump = pump_index + 1
            current_balance = 0
    return start_pump if total_balance >= 0 else -1


if __name__ == '__main__':
    total_pumps = int(input())
    pumps_list = [(int(part[0]), int(part[1])) for part in (input().split() for _ in range(total_pumps))]
    first_pump_index = get_starting_pump(pumps=pumps_list)
    print(first_pump_index)
