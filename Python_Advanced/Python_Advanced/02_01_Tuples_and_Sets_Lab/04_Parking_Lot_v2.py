def manage_parking_lot(number_of_commands: int) -> set[str]:
    """
    Manage the parking lot by recording cars entering and leaving.

    Args:
        number_of_commands (int): Total number of commands.

    Returns:
        set[str]: Set with car numbers still in the parking lot.
    """
    parking_lot = set()
    for _ in range(number_of_commands):
        command_info = input().split(', ')
        direction = command_info[0]
        car_number = command_info[1]
        if direction == 'IN':
            parking_lot.add(car_number)
        elif direction == 'OUT':
            parking_lot.discard(car_number)
    return parking_lot


if __name__ == '__main__':
    commands_count = int(input())
    parking_cars = manage_parking_lot(number_of_commands=commands_count)
    if parking_cars:
        for car in parking_cars:
            print(car)
    else:
        print('Parking Lot is Empty')
