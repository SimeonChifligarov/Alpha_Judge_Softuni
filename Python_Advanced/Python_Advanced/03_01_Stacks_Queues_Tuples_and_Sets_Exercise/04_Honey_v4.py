from collections import deque


def produce_honey(bee_values: list[int], nectar_values: list[int], operator_values: list[str]) -> None:
    """
    This function checks bees and nectar, and makes honey by using math symbols.

    Args:
        bee_values (list[int]): The list of bees.
        nectar_values (list[int]): The list of nectar.
        operator_values (list[str]): The list of math symbols.

    Returns:
        None
    """
    bees = deque(bee_values)
    nectar = deque(nectar_values[::-1])
    symbols = deque(operator_values)
    honey_collected = 0
    operations = {
        '+': lambda a, b: abs(a + b),
        '-': lambda a, b: abs(a - b),
        '*': lambda a, b: abs(a * b),
        '/': lambda a, b: abs(a / b) if b != 0 else 0,
    }
    while bees and nectar:
        bee = bees[0]
        current_nectar = nectar[0]
        if current_nectar < bee:
            nectar.popleft()
            continue
        sign = symbols.popleft()
        if current_nectar == 0 and sign == '/':
            bees.popleft()
            nectar.popleft()
            continue
        honey_collected += operations[sign](bee, current_nectar)
        bees.popleft()
        nectar.popleft()
    print(f'Total honey made: {honey_collected}')
    if bees:
        print(f"Bees left: {', '.join(str(x) for x in bees)}")
    if nectar:
        print(f"Nectar left: {', '.join(str(x) for x in reversed(nectar))}")


if __name__ == '__main__':
    bees_sequence = [int(x) for x in input().split()]
    nectar_sequence = [int(x) for x in input().split()]
    symbols_sequence = input().split()
    produce_honey(bee_values=bees_sequence, nectar_values=nectar_sequence, operator_values=symbols_sequence)
