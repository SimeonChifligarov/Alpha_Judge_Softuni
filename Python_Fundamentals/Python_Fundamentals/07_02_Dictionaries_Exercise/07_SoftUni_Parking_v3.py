def parking_validation():
    """Handles parking registration and unregistration system."""
    n = int(input())
    parking_db = {}

    for _ in range(n):
        command = input().split()
        action = command[0]
        username = command[1]

        if action == 'register':
            license_plate = command[2]
            if username in parking_db:
                print(f'ERROR: already registered with plate number {parking_db[username]}')
            else:
                parking_db[username] = license_plate
                print(f'{username} registered {license_plate} successfully')

        elif action == 'unregister':
            if username not in parking_db:
                print(f'ERROR: user {username} not found')
            else:
                del parking_db[username]
                print(f'{username} unregistered successfully')

    for user, plate in parking_db.items():
        print(f'{user} => {plate}')


if __name__ == '__main__':
    parking_validation()
