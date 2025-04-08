from collections import deque
from typing import List


def hot_potato_game(children: List[str], toss_number: int) -> None:
    """
    Simulates the Hot Potato game by removing every nth kid until one remains.
    Prints out each removal and the last kid remaining.
    """
    queue = deque(children)
    while len(queue) > 1:
        for _ in range(toss_number - 1):
            queue.append(queue.popleft())
        removed_kid = queue.popleft()
        print(f'Removed {removed_kid}')

    last_kid = queue.popleft()
    print(f'Last is {last_kid}')


if __name__ == '__main__':
    kids_names_input = input().split()
    toss_count_input = int(input())
    hot_potato_game(children=kids_names_input, toss_number=toss_count_input)
