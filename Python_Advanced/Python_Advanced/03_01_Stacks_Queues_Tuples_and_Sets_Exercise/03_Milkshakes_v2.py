from collections import deque


def make_milkshakes(chocolate_pieces: list[int], milk_cups: list[int]) -> None:
    """
    This function tries to make chocolate milkshakes by matching chocolate and milk values.

    Args:
        chocolate_pieces (list[int]): List of chocolate amounts.
        milk_cups (list[int]): List of milk amounts.

    Returns:
        None
    """
    chocolates = chocolate_pieces
    milks = deque(milk_cups)
    milkshake_count = 0
    while chocolates and milks and milkshake_count < 5:
        while chocolates and chocolates[-1] <= 0:
            chocolates.pop()
        while milks and milks[0] <= 0:
            milks.popleft()
        if not chocolates or not milks:
            break
        current_chocolate = chocolates[-1]
        current_milk = milks[0]
        if current_chocolate == current_milk:
            milkshake_count += 1
            chocolates.pop()
            milks.popleft()
        else:
            milks.append(milks.popleft())
            chocolates[-1] -= 5
    if milkshake_count == 5:
        print('Great! You made all the chocolate milkshakes needed!')
    else:
        print('Not enough milkshakes.')
    if chocolates:
        print(f"Chocolate: {', '.join(str(x) for x in chocolates)}")
    else:
        print('Chocolate: empty')
    if milks:
        print(f"Milk: {', '.join(str(x) for x in milks)}")
    else:
        print('Milk: empty')


if __name__ == '__main__':
    chocolates_input = [int(x) for x in input().split(', ')]
    milks_input = [int(x) for x in input().split(', ')]
    make_milkshakes(chocolate_pieces=chocolates_input, milk_cups=milks_input)
