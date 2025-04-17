from collections import deque


def prepare_milkshakes(choco_stack: list[int], milk_queue: list[int]) -> None:
    """
    This function makes milkshakes by matching chocolates and milk based on simple rules.

    Args:
        choco_stack (list[int]): List with chocolate values.
        milk_queue (list[int]): List with milk values.

    Returns:
        None
    """
    chocolates = deque(choco_stack[::-1])
    milks = deque(milk_queue)
    shakes_made = 0
    while chocolates and milks and shakes_made < 5:
        current_choco = chocolates[-1]
        current_milk = milks[0]
        if current_choco <= 0:
            chocolates.pop()
            continue
        if current_milk <= 0:
            milks.popleft()
            continue
        if current_choco == current_milk:
            chocolates.pop()
            milks.popleft()
            shakes_made += 1
        else:
            milks.append(milks.popleft())
            chocolates[-1] -= 5
    print('Great! You made all the chocolate milkshakes needed!' if shakes_made == 5 else 'Not enough milkshakes.')
    print(f"Chocolate: {', '.join(str(num) for num in reversed(chocolates))}" if chocolates else 'Chocolate: empty')
    print(f"Milk: {', '.join(str(num) for num in milks)}" if milks else 'Milk: empty')


if __name__ == '__main__':
    chocolates_data = [int(el) for el in input().split(', ')]
    milks_data = [int(el) for el in input().split(', ')]
    prepare_milkshakes(choco_stack=chocolates_data, milk_queue=milks_data)
