from collections import deque


def cup_filling(bottles_sequence: list[int], cups_sequence: list[int]) -> None:
    """
    This function fills cups using bottles.
    It shows what remains and how much water is wasted.

    Args:
        bottles_sequence: List of bottles with water.
        cups_sequence: List of cups to be filled.

    Returns:
        None
    """
    bottles = bottles_sequence
    cups = deque(cups_sequence)
    wasted = 0

    while bottles and cups:
        bottle = bottles.pop()
        cup = cups.popleft()

        while True:
            if bottle >= cup:
                wasted += bottle - cup
                break
            else:
                cup -= bottle
                if not bottles:
                    cups.appendleft(cup)
                    break
                bottle = bottles.pop()

    if not cups:
        print(f"Bottles: {' '.join(str(b) for b in reversed(bottles))}")
    else:
        print(f"Cups: {' '.join(str(c) for c in cups)}")

    print(f'Wasted litters of water: {wasted}')


if __name__ == '__main__':
    cups_input_list = [int(x) for x in input().split()]
    bottles_input_list = [int(x) for x in input().split()]

    cup_filling(
        bottles_sequence=bottles_input_list,
        cups_sequence=cups_input_list
    )
