def manage_parking(commands_list: list[str]) -> set[str]:
    """
    Keep track of cars entering and leaving the parking lot.

    Args:
        commands_list (list[str]): List with commands.

    Returns:
        set[str]: Set with car numbers still parked.
    """
    parked_cars = set()
    for command in commands_list:
        action, car_plate = command.split(', ')
        parked_cars.add(car_plate) if action == 'IN' else parked_cars.discard(car_plate)
    return parked_cars


if __name__ == '__main__':
    total_commands = int(input())
    commands_input = [input() for _ in range(total_commands)]
    current_parking = manage_parking(commands_list=commands_input)
    if current_parking:
        for car_number in current_parking:
            print(car_number)
    else:
        print('Parking Lot is Empty')
