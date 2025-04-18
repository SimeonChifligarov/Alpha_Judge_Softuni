from collections import deque


def gather_honey(bees_seq: list[int], nectar_seq: list[int], symbols_seq: list[str]) -> None:
    """
    This function matches bees and nectar and makes honey by simple math rules.

    Args:
        bees_seq (list[int]): List with bees' values.
        nectar_seq (list[int]): List with nectar values.
        symbols_seq (list[str]): List with math operation symbols.

    Returns:
        None
    """
    bees = deque(bees_seq)
    nectar = nectar_seq
    symbols = deque(symbols_seq)
    total_honey = 0
    while bees and nectar:
        bee = bees[0]
        nectar_value = nectar[-1]
        if nectar_value < bee:
            nectar.pop()
            continue
        symbol = symbols.popleft()
        # result = ''
        if symbol == '+':
            result = abs(bee + nectar_value)
        elif symbol == '-':
            result = abs(bee - nectar_value)
        elif symbol == '*':
            result = abs(bee * nectar_value)
        elif symbol == '/':
            if nectar_value == 0:
                bees.popleft()
                nectar.pop()
                continue
            result = abs(bee / nectar_value)
        total_honey += result
        bees.popleft()
        nectar.pop()
    print(f'Total honey made: {total_honey}')
    if bees:
        print(f"Bees left: {', '.join(str(x) for x in bees)}")
    if nectar:
        print(f"Nectar left: {', '.join(str(x) for x in nectar)}")


if __name__ == '__main__':
    bees_data = [int(x) for x in input().split()]
    nectar_data = [int(x) for x in input().split()]
    symbols_data = input().split()
    gather_honey(bees_seq=bees_data, nectar_seq=nectar_data, symbols_seq=symbols_data)
