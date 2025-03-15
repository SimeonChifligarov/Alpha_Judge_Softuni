def manage_force_users() -> dict[str, list[str]]:
    """
    Reads force users and their force sides from input.
    Returns a dictionary where keys are force sides and values are lists of unique force users.
    """
    force_sides = {}
    force_users = {}

    while True:
        data = input()
        if data == 'Lumpawaroo':
            break

        if ' | ' in data:
            force_side, force_user = data.split(' | ', maxsplit=1)

            if force_user not in force_users:
                if force_side not in force_sides:
                    force_sides[force_side] = []

                force_users[force_user] = force_side
                force_sides[force_side].append(force_user)

        elif ' -> ' in data:
            force_user, force_side = data.split(' -> ', maxsplit=1)

            if force_user in force_users:
                old_side = force_users[force_user]
                force_sides[old_side].remove(force_user)

            if force_side not in force_sides:
                force_sides[force_side] = []

            force_users[force_user] = force_side
            force_sides[force_side].append(force_user)
            print(f'{force_user} joins the {force_side} side!')

    return force_sides


def print_force_sides(force_sides: dict[str, list[str]]) -> None:
    """
    Prints each force side and its force users.
    """
    for side, users in force_sides.items():
        if users:
            print(f'Side: {side}, Members: {len(users)}')
            for user in users:
                print(f'! {user}')


if __name__ == '__main__':
    force_data = manage_force_users()
    print_force_sides(force_sides=force_data)
