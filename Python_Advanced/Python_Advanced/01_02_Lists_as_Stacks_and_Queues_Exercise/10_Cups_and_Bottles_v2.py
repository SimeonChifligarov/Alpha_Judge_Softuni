from collections import deque


def fill_cups(cups_list: list[int], bottles_list: list[int]) -> None:
    """
    This function fills cups using water from bottles.
    It shows if cups are filled and how much water is wasted.

    Args:
        cups_list: List of cup capacities.
        bottles_list: List of bottle capacities.

    Returns:
        None
    """
    cups = deque(cups_list)
    bottles = bottles_list
    wasted_water = 0

    while cups and bottles:
        current_cup = cups[0]
        current_bottle = bottles.pop()

        if current_bottle >= current_cup:
            wasted_water += current_bottle - current_cup
            cups.popleft()
        else:
            cups[0] -= current_bottle

    if not cups:
        print(f"Bottles: {' '.join(str(bottle) for bottle in reversed(bottles))}")
    else:
        print(f"Cups: {' '.join(str(cup) for cup in cups)}")

    print(f'Wasted litters of water: {wasted_water}')


if __name__ == '__main__':
    cups_input = [int(el) for el in input().split()]
    bottles_input = [int(el) for el in input().split()]

    fill_cups(
        cups_list=cups_input,
        bottles_list=bottles_input
    )
