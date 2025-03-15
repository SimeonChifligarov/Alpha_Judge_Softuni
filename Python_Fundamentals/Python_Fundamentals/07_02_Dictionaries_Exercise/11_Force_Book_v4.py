def manage_force_users():
    force_sides = {}

    while True:
        command = input()
        if command == 'Lumpawaroo':
            break

        if ' | ' in command:
            force_side, force_user = command.split(' | ', maxsplit=1)
            if not any(force_user in users for users in force_sides.values()):
                force_sides.setdefault(force_side, list()).append(force_user)

        elif ' -> ' in command:
            force_user, force_side = command.split(' -> ', maxsplit=1)
            for side, users in force_sides.items():
                if force_user in users:
                    users.remove(force_user)
                    break

            force_sides.setdefault(force_side, list()).append(force_user)
            print(f'{force_user} joins the {force_side} side!')

    # for side, users in sorted(force_sides.items(), key=lambda x: (-len(x[1]), x[0])):
    for side, users in force_sides.items():
        if users:
            print(f'Side: {side}, Members: {len(users)}')
            for user in users:
                print(f'! {user}')


if __name__ == '__main__':
    manage_force_users()
