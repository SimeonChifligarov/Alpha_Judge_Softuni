from typing import List


def manage_gift_list(gifts: List[str]) -> List[str]:
    """
    Manages the list of gifts based on received commands until 'No Money' is encountered.
    """
    while True:
        command = input()
        if command == 'No Money':
            break

        parts = command.split()
        action = parts[0]

        if action == 'OutOfStock':
            gift = parts[1]
            gifts = ['None' if g == gift else g for g in gifts]
        elif action == 'Required':
            gift = parts[1]
            index = int(parts[2])
            if 0 <= index < len(gifts):
                gifts[index] = gift
        elif action == 'JustInCase':
            gift = parts[1]
            gifts[-1] = gift

    return gifts


if __name__ == '__main__':
    gifts_input = input().split()
    updated_gifts = manage_gift_list(gifts=gifts_input)
    print(' '.join(gift for gift in updated_gifts if gift != 'None'))
