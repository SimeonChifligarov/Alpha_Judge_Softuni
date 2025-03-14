def register_user(parking_data: dict[str, str], username: str, license_plate: str) -> None:
    """
    Registers a user with a license plate if not already registered.
    Prints appropriate messages based on the registration status.
    """
    if username in parking_data:
        print(f'ERROR: already registered with plate number {parking_data[username]}')
    else:
        parking_data[username] = license_plate
        print(f'{username} registered {license_plate} successfully')


def unregister_user(parking_data: dict[str, str], username: str) -> None:
    """
    Unregisters a user if they exist in the parking database.
    Prints appropriate messages based on the unregistration status.
    """
    if username not in parking_data:
        print(f'ERROR: user {username} not found')
    else:
        del parking_data[username]
        print(f'{username} unregistered successfully')


def process_parking_commands() -> None:
    """
    Reads input commands and processes them accordingly.
    After all commands, prints the final state of the parking registrations.
    """
    n = int(input())
    parking_data = {}

    for _ in range(n):
        command_parts = input().split()
        action, username = command_parts[0], command_parts[1]

        if action == 'register':
            register_user(parking_data=parking_data, username=username, license_plate=command_parts[2])
        elif action == 'unregister':
            unregister_user(parking_data=parking_data, username=username)

    for user, plate in parking_data.items():
        print(f'{user} => {plate}')


if __name__ == '__main__':
    process_parking_commands()
