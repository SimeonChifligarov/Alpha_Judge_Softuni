from collections import deque


def make_honey(bees_list: list[int], nectar_list: list[int], operators_list: list[str]) -> None:
    """
    This function matches bees and nectar and calculates honey made with math operations.

    Args:
        bees_list (list[int]): List with bees' power values.
        nectar_list (list[int]): List with nectar amounts.
        operators_list (list[str]): List with operators for honey making.

    Returns:
        None
    """
    bees = deque(bees_list)
    nectar = nectar_list
    operators = deque(operators_list)
    total_honey = 0
    actions = {
        '+': lambda x, y: abs(x + y),
        '-': lambda x, y: abs(x - y),
        '*': lambda x, y: abs(x * y),
        '/': lambda x, y: abs(x / y) if y != 0 else 0,
    }
    while bees and nectar:
        current_bee = bees[0]
        current_nectar = nectar[-1]
        if current_nectar >= current_bee:
            operation = operators.popleft()
            if current_nectar == 0 and operation == '/':
                bees.popleft()
                nectar.pop()
                continue
            total_honey += actions[operation](current_bee, current_nectar)
            bees.popleft()
            nectar.pop()
        else:
            nectar.pop()
    print(f'Total honey made: {total_honey}')
    if bees:
        print(f"Bees left: {', '.join(str(b) for b in bees)}")
    if nectar:
        print(f"Nectar left: {', '.join(str(n) for n in nectar)}")


if __name__ == '__main__':
    bees_input = [int(el) for el in input().split()]
    nectar_input = [int(el) for el in input().split()]
    operators_input = input().split()
    make_honey(bees_list=bees_input, nectar_list=nectar_input, operators_list=operators_input)
