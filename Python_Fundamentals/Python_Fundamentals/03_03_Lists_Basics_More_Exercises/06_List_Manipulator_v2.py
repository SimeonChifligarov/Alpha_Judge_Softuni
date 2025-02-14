from typing import List


def exchange_list(lst: List[int], index: int) -> List[int]:
    """Exchanges the list after the given index."""
    if 0 <= index < len(lst):
        return lst[index + 1:] + lst[:index + 1]
    else:
        print('Invalid index')
        return lst


def find_max_index(lst: List[int], parity: str) -> None:
    """Finds the index of the max even/odd element."""
    filtered = [i for i in range(len(lst)) if (lst[i] % 2 == 0) == (parity == 'even')]
    if filtered:
        max_index = max(filtered, key=lambda i: (lst[i], i))
        print(max_index)
    else:
        print('No matches')


def find_min_index(lst: List[int], parity: str) -> None:
    """Finds the index of the min even/odd element."""
    filtered = [i for i in range(len(lst)) if (lst[i] % 2 == 0) == (parity == 'even')]
    if filtered:
        min_index = min(filtered, key=lambda i: (lst[i], -i))
        print(min_index)
    else:
        print('No matches')


def first_elements(lst: List[int], count: int, parity: str) -> None:
    """Finds the first count even/odd elements."""
    if count > len(lst):
        print('Invalid count')
        return
    result = [x for x in lst if (x % 2 == 0) == (parity == 'even')][:count]
    print(result)


def last_elements(lst: List[int], count: int, parity: str) -> None:
    """Finds the last count even/odd elements."""
    if count > len(lst):
        print('Invalid count')
        return
    result = [x for x in lst if (x % 2 == 0) == (parity == 'even')][-count:]
    print(result)


if __name__ == '__main__':
    lst = list(map(int, input().split()))

    while True:
        command = input()
        if command == 'end':
            break

        parts = command.split()
        action = parts[0]

        if action == 'exchange':
            index = int(parts[1])
            lst = exchange_list(lst=lst, index=index)
        elif action == 'max':
            find_max_index(lst=lst, parity=parts[1])
        elif action == 'min':
            find_min_index(lst=lst, parity=parts[1])
        elif action == 'first':
            count = int(parts[1])
            first_elements(lst=lst, count=count, parity=parts[2])
        elif action == 'last':
            count = int(parts[1])
            last_elements(lst=lst, count=count, parity=parts[2])

    print(f'[{", ".join(map(str, lst))}]')
