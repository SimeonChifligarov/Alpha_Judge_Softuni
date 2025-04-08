from collections import deque


def manage_water_queue() -> None:
    """
    Handles a queue for a water dispenser with commands for serving water and refilling.
    """
    water_quantity = int(input())
    waiting_people = deque()

    input_line = input()
    while input_line != 'Start':
        waiting_people.append(input_line)
        input_line = input()

    command_input = input()
    while command_input != 'End':
        parts = command_input.split()
        if parts[0] == 'refill':
            water_quantity += int(parts[1])
        else:
            needed_water = int(parts[0])
            current_client = waiting_people.popleft()
            if needed_water <= water_quantity:
                water_quantity -= needed_water
                print(f'{current_client} got water')
            else:
                print(f'{current_client} must wait')
        command_input = input()
    print(f'{water_quantity} liters left')


if __name__ == '__main__':
    manage_water_queue()
