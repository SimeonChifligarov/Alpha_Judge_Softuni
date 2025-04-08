from collections import deque


def water_dispenser_management() -> None:
    """
    Manages a water dispenser queue based on initial water quantity and subsequent commands.
    Handles people getting water or refilling the dispenser.
    """
    available_water = int(input())
    people_queue = deque()
    while True:
        person = input()
        if person == 'Start':
            break
        people_queue.append(person)

    while True:
        command = input()
        if command == 'End':
            break

        if command.startswith('refill'):
            _, refill_amount = command.split()
            available_water += int(refill_amount)
        else:
            requested_water = int(command)
            current_person = people_queue.popleft()
            if requested_water <= available_water:
                available_water -= requested_water
                print(f'{current_person} got water')
            else:
                print(f'{current_person} must wait')

    print(f'{available_water} liters left')


if __name__ == '__main__':
    water_dispenser_management()
