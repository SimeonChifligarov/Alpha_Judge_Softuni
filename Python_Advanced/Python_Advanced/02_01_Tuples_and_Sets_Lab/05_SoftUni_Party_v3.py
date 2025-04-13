def find_absent_guests(invited_guests: set[str], incoming_guests: str) -> tuple[list[str], list[str]]:
    """
    Find all guests who did not come to the party.

    Args:
        invited_guests (set[str]): Set with all invited guests.
        incoming_guests (str): Single string with all incoming guest entries separated by newline.

    Returns:
        tuple[list[str], list[str]]: Sorted lists of VIP and Regular missing guests.
    """
    arrivals = incoming_guests.split('\n')
    for guest in arrivals:
        if guest != 'END':
            invited_guests.discard(guest)
    vip_missing = sorted(guest for guest in invited_guests if guest[0].isdigit())
    regular_missing = sorted(guest for guest in invited_guests if not guest[0].isdigit())
    return vip_missing, regular_missing


if __name__ == '__main__':
    guests_number = int(input())
    invited_set = {input() for _ in range(guests_number)}
    arrivals_input = []
    while True:
        line = input()
        arrivals_input.append(line)
        if line == 'END':
            break
    arrivals_text = '\n'.join(arrivals_input)
    vip_list, regular_list = find_absent_guests(invited_guests=invited_set, incoming_guests=arrivals_text)
    missing_guests_total = vip_list + regular_list
    print(len(missing_guests_total))
    for missing_guest in missing_guests_total:
        print(missing_guest)
