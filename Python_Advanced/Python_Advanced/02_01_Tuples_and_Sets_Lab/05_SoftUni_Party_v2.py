def get_missing_guests(all_guests: list[str], arrived_guests: list[str]) -> tuple[list[str], list[str]]:
    """
    Find guests who did not come to the party.

    Args:
        all_guests (list[str]): List of all invited guests.
        arrived_guests (list[str]): List of guests who arrived.

    Returns:
        tuple[list[str], list[str]]: VIP and Regular guests who did not come.
    """
    invited_set = set(all_guests)
    arrived_set = set(arrived_guests)
    missing_guests = invited_set - arrived_set
    vip_guests = sorted([guest for guest in missing_guests if guest[0].isdigit()])
    regular_guests = sorted([guest for guest in missing_guests if not guest[0].isdigit()])
    return vip_guests, regular_guests


if __name__ == '__main__':
    number_of_invitations = int(input())
    invited_list = [input() for _ in range(number_of_invitations)]
    arrived_list = []
    while True:
        guest_entry = input()
        if guest_entry == 'END':
            break
        arrived_list.append(guest_entry)
    vip_missing, regular_missing = get_missing_guests(all_guests=invited_list, arrived_guests=arrived_list)
    total_missing = vip_missing + regular_missing
    print(len(total_missing))
    for guest_code in total_missing:
        print(guest_code)
